import os
from dotenv import load_dotenv
import numpy as np
import cv2
import imutils
import supervisely as sly
# load ENV variables for debug
# has no effect in production
load_dotenv(os.path.expanduser("~/supervisely.env"))
load_dotenv("local.env")

class_qr = None

def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def transform_n_qrdetect(local_path, local_result_path):
    image = cv2.imread(local_path)
    orig_height = image.shape[0]
    orig_wid = image.shape[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    # loop over the contours
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break

    image_to_cntr = image.copy()
    countered_img = cv2.drawContours(image_to_cntr, [screenCnt], -1, (0, 255, 0), 2)

    pts = np.array(screenCnt.reshape(4,2),dtype="float32")
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

    matrix = [
	[int(max(tl)), int(min(tl))],
	[int(max(tl)) + int(widthB) - 1, int(min(tl))],
	[int(max(tl)) + int(widthB) - 1, int(min(tl)) + int(widthB) - 1],
	[int(max(tl)),int(min(tl)) + int(widthB) - 1]]

    dst = np.array(matrix, dtype = "float32")
    
    polygon = sly.Polygon(exterior=[
        sly.PointLocation(int(min(tl)), int(max(tl))), 
        sly.PointLocation(int(min(tl)), int(max(tl)) + int(widthB)), 
        sly.PointLocation(int(min(tl)) + int(widthB), int(max(tl)) + int(widthB)),
        sly.PointLocation(int(min(tl)) + int(widthB), int(max(tl)))
    ])

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(src=image, M=M, dsize=(orig_wid, orig_height))

    detector = cv2.QRCodeDetector()
    data, vertices_array, bin_qr = detector.detectAndDecode(countered_img)

    tags = sly.TagCollection(items=list[
        "QR_edge": int(data),
        "area": int(data) * int(data),
        "measure":"cm"])

    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There is no QR code or program has failed to detect it it.") 

    cv2.imwrite(local_result_path, warped)

    return polygon, tags

def main():
    global class_qr

    api = sly.Api.from_env()
    project_id = int(os.environ["PROJECT_ID"])
    project = api.project.get_info_by_id(project_id)
    if project is None:
        raise KeyError(f"Project with ID {project_id} not found in your account")
    print(f"Project info: {project.name} (id={project.id})")

    new_project = api.project.create(project.workspace_id, project.name + "_transformed", description="perspective trasformation" ,change_name_if_conflict=True)
    class_qr = sly.ObjClass(name="QR", geometry_type=sly.Polygon, color=[0, 255, 0])
    new_meta = sly.ProjectMeta(obj_classes=[class_qr])
    api.project.update_meta(new_project.id, new_meta)

    datasets = api.dataset.get_list(project.id)
    progress = sly.Progress("Processing...", project.items_count)
    for dataset in datasets:
        new_dataset = api.dataset.create(new_project.id, dataset.name)
        images = api.image.get_list(dataset.id)
        for image in images:
            local_path = os.path.join("src", image.name)    
            api.image.download_path(image.id, local_path)
            res_name = "res_" + image.name
            local_result_path = os.path.join("src", res_name)
            polygon, tags = transform_n_qrdetect(local_path, local_result_path)
            new_image = api.image.upload_path(new_dataset.id, image.name, local_result_path)
            label = sly.Label(geometry=polygon, tags=tags, obj_class=class_qr)
            new_ann = sly.Annotation(img_size=[new_image.height, new_image.width], labels=[label])
            api.annotation.upload_ann(new_image.id, new_ann)

            sly.fs.silent_remove(local_path)
            sly.fs.silent_remove(local_result_path)
            progress.iter_done_report()
    print("Done")
    
    if sly.is_production():
        task_id = sly.env.task_id()
        api.task.set_output_project(task_id, new_project.id, new_project.name)

if __name__ == "__main__":
    main()