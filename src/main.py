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

def main():
    def order_points(pts):
        rect = np.zeros((4, 2), dtype = "float32")
        s = pts.sum(axis = 1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        diff = np.diff(pts, axis = 1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect

    def four_point_transform(image, pts):
        rect = order_points(pts)
        (tl, tr, br, bl) = rect
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

        fin_tl_x, fin_tl_y = int(max(tl)), int(min(tl))
        fin_tr_x, fin_tr_y = int(max(tl)) + int(widthB) - 1, int(min(tl))
        fin_br_x, fin_br_y = int(max(tl)) + int(widthB) - 1, int(min(tl)) + int(widthB) - 1
        fin_bl_x, fin_bl_y = int(max(tl)),int(min(tl)) + int(widthB) - 1

        dst = np.array([
		[fin_tl_x, fin_tl_y],
		[fin_tr_x, fin_tr_y],
		[fin_br_x, fin_br_y],
		[fin_bl_x, fin_bl_y]], dtype = "float32")

        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(src=image, M=M, dsize=(orig_wid, orig_height))

        return warped 
   
    def run_n_qrdetect(local_path, local_result_path):
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
        warped = four_point_transform(image, pts)

        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_qr = detector.detectAndDecode(countered_img)

        if vertices_array is not None:
            print("QRCode data:")
            print(data)
        else:
            print("There is no QR code or program has failed to detect it it.") 

        cv2.imwrite(local_result_path, warped)
    
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    remote_dir = sly.env.folder()
    files_info = api.file.list2(team_id, remote_dir)

    progress = sly.Progress("Processing...", len(files_info))
    for info in files_info:
        remote_path = info.path
        # remote_path = sly.env.file()
        if sly.image.has_valid_ext(remote_path) is False:
            progress.iter_done_report()
            continue

        local_path = os.path.join("src", sly.fs.get_file_name_with_ext(remote_path))
        api.file.download(team_id, remote_path, local_path)

        result_name = (
            sly.fs.get_file_name(local_path)
            + "_transformed"
            + sly.fs.get_file_ext(local_path)
        )
        local_result_path = os.path.join("src", result_name)
        run_n_qrdetect(local_path, local_result_path)

        remote_result_path = os.path.join(os.path.dirname(remote_path), result_name)
        if api.file.exists(team_id, remote_result_path) is True:
            api.file.remove(team_id, remote_result_path)
        api.file.upload(team_id, local_result_path, remote_result_path)

        sly.fs.silent_remove(local_path)
        sly.fs.silent_remove(local_result_path)

        progress.iter_done_report()
    
    print("Done")
    
    if sly.is_production():
        task_id = sly.env.task_id()
        file_info = api.file.get_info_by_path(team_id, remote_result_path)
        api.task.set_output_directory(task_id, file_info.id, remote_dir)

if __name__ == "__main__":
    main()