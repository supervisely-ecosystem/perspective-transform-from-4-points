<!-- <div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/202196829-fc71bc02-73b0-40a4-a02a-1e1ac9cad13e.jpg"/>  

# Perspective transform using QR code

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/perspective-transform-using-qr-code)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/perspective-transform-using-qr-code)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/perspective-transform-using-qr-code)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/perspective-transform-using-qr-code)](https://supervise.ly)

</div>

# Overview

App iterates over all datasets in a project and creates new project with the perspective transformed pictures. App is useful for certain tasks that usually involve taking lots of pictures and then labeling them.
Also, this app creates polygon object of QR code, which allows for easier calculations upon labeling.

Typical usecase is the following: you need to take pictures and label a lot of objects of the same type, let's say, calculate their areas, and need to keep track of each object via QR code. This app standardizes each picture by perspective transforming it, and creates polygon on top of the QR code for easier calculation.

This app also works without QR code, but needs to be provided with clearly visible square in images.

# How to Run

1. Go to your Workspace

<img src="https://user-images.githubusercontent.com/115161827/202218609-485003e6-e295-4d3b-9bd5-fa302e43eea2.png">

2. Run app from context menu
<img src="https://user-images.githubusercontent.com/115161827/202220220-ff76d5d4-20b1-40ac-a0b3-8e2416131c4e.gif">

3. Upload images into new directory using drag-and-drop
  <img src="https://user-images.githubusercontent.com/115161827/202231709-a964351f-390f-41be-a685-4489d9845c33.gif">

4. Right click to directory and run the app from the context menu
<img src="https://user-images.githubusercontent.com/115161827/202220693-788ba804-6fc5-4ddd-87b3-494f459374d9.png">


## Result

As a result of running this app, images with youtube button will be created in the same directory with modified names (`_youtube` will be added to the file names)

<img src="https://user-images.githubusercontent.com/115161827/202250089-ff3083e3-50d9-4c1d-ba60-3f0cb93d75e4.gif" width="80%" style='padding-top: 10px'>

Then you can add the following code snippet to your README (do not forget to replace links in example):

```md
<a data-key="sly-embeded-video-link" href="https://youtu.be/e47rWdgK-_M" data-video-code="e47rWdgK-_M">
    <img src="https://i.imgur.com/sJdEEkN.png" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;">
</a>
```

Once you added it to your readme, it will be shown nicely in both Supervisely platform and GitHub.


In Supervisely  |  In GitHub
:-------------------------:|:-----------------------------------:
<img src="https://user-images.githubusercontent.com/115161827/202243190-fe28997c-2c70-46dd-9f15-9122b4ce9ad4.png" style="max-height: 300px; width: auto;"/>  |  <img src="https://user-images.githubusercontent.com/115161827/202243009-3e17cd2a-08ef-4636-9ed0-109b662dfe63.png" style="max-height: 300px; width: auto;"/> -->