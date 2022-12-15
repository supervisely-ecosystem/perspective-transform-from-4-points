<div align="center" markdown>
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

App iterates over all datasets in a project and creates new project with the perspective transformed images. This is useful for certain tasks that usually involve taking lots of pictures and then labeling them.
Also, this app creates polygon object of QR code, which allows for easier calculations upon labeling.

Typical usecase is the following: you need to take pictures and label a lot of objects of the same type, let's say, calculate their areas, and need to keep track of each object via QR code. This app standardizes each picture by perspective transforming it, and creates polygon on top of the QR code for easier calculation.

App also reads QR code data, and if the value of code is a number, more precisely the lengh of one of the edges, polygon will also have a tag with that value and a tag with calculated area.

# How to Run

1. Go to your Workspace

<img src="https://user-images.githubusercontent.com/115161827/202218609-485003e6-e295-4d3b-9bd5-fa302e43eea2.png">

2. Right click to the project and run app from context menu

<img src="https://user-images.githubusercontent.com/115161827/202220220-ff76d5d4-20b1-40ac-a0b3-8e2416131c4e.gif">


## Result

As a result of running this app, you will be left with one more project with modified name, that has all the datasets and images as the original.

<img src="https://user-images.githubusercontent.com/115161827/202250089-ff3083e3-50d9-4c1d-ba60-3f0cb93d75e4.gif" width="80%" style='padding-top: 10px'>


Before  |  After
:-------------------------:|:-----------------------------------:
<img src="https://user-images.githubusercontent.com/115161827/202243190-fe28997c-2c70-46dd-9f15-9122b4ce9ad4.png" style="max-height: 300px; width: auto;"/>  |  <img src="https://user-images.githubusercontent.com/115161827/202243009-3e17cd2a-08ef-4636-9ed0-109b662dfe63.png" style="max-height: 300px; width: auto;"/>