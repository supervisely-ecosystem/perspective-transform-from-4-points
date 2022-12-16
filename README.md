<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/208094131-d3ab5fcf-3da3-476b-bd50-e563deaf9b72.jpg"/>  

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

App iterates over all datasets in a project and creates new project with the perspective transformed images. This is useful for certain tasks that usually involve taking lots of pictures and then labeling them.
Also, this app creates polygon object of QR code, which allows for easier calculations upon labeling.

Typical usecase is the following: you need to take pictures and label a lot of objects of the same type, let's say, calculate their areas, and need to keep track of each object via QR code. This app standardizes each picture by perspective transforming it, and creates polygon on top of the QR code for easier calculation.

App also reads QR code data, and if the value of code is a number, more precisely the lengh of one of the edges, polygon will also have a tag with that value and a tag with calculated area.

# How to Run

1. Go to your Workspace

<img src="https://user-images.githubusercontent.com/115161827/207947458-acc8a67a-5274-4df4-88bb-661fb9815599.png">

2. Right click to the project and run app from context menu

<img src="https://user-images.githubusercontent.com/115161827/207949467-d45542ff-b7aa-41f1-b75a-65b8d6b891ba.gif">


## Result

As a result of running this app, you will be left with one more project with modified name, that has all the datasets and images as the original.

<img src="https://user-images.githubusercontent.com/115161827/207947931-295a385f-4235-4525-825b-7c3192dbd38e.png">


Before  |  After
:-------------------------:|:-----------------------------------:
<img src="https://user-images.githubusercontent.com/115161827/207944480-391b1d35-eb30-43e7-8da1-5ac7b810a0f9.png" style="max-height: 300px; width: auto;"/>  |  <img src="https://user-images.githubusercontent.com/115161827/207945669-6932873b-0b2d-41d8-8654-decdc7b5f85b.png" style="max-height: 300px; width: auto;"/>