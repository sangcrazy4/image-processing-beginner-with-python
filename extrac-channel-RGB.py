# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:13:13 2018

@author: sangcrazy4
"""

import numpy as np
import cv2

# Load an color image in grayscale
image_grayscale = cv2.imread('images/tomato.jpg',0)
# Load an color image in RGB
image = cv2.imread('images/tomato.jpg')

image_red_channel = image[:,:,2]
image_green_channel = image[:,:,1]
image_blue_channel = image[:,:,0]

numpy_horizontal_top = np.hstack((image_grayscale, image_red_channel))
numpy_horizontal1_down = np.hstack((image_green_channel, image_blue_channel))
numpy_4_channel = np.concatenate((numpy_horizontal_top, numpy_horizontal1_down), axis=0)

cv2.imshow('Extec-channel-with-1D', numpy_4_channel)

image_blue = image.copy()
# set green and red channels to 0
image_blue[:, :, 1] = 0
image_blue[:, :, 2] = 0

image_green = image.copy()
# set blue and red channels to 0
image_green[:, :, 0] = 0
image_green[:, :, 2] = 0

image_red = image.copy()
# set blue and green channels to 0
image_red[:, :, 0] = 0
image_red[:, :, 1] = 0

numpy_horizontal_top_3d = np.hstack((image, image_red))
numpy_horizontal1_down_3d = np.hstack((image_green, image_blue))
numpy_4_channel_3d = np.concatenate((numpy_horizontal_top_3d, numpy_horizontal1_down_3d), axis=0)

cv2.imshow('Extec-channel-with-3D', numpy_4_channel_3d)

cv2.waitKey(0)
cv2.destroyAllWindows()
