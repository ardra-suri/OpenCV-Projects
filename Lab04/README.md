# Image Processing Toolbox

This Python program is an Image Processing Toolbox providing various features for modifying and enhancing images. It utilizes the OpenCV and NumPy libraries for image processing and manipulation.

## Features

### Add Salt and Pepper Noise

- Adds salt and pepper noise to the input image.
- Adjustable probability parameter controls the density of noise.

### Display Noisy Image

- Displays the image with added salt and pepper noise.

### Smooth with 3x3 Box-Kernel

- Smoothens the noisy image using a 3x3 box-kernel convolution.
- Improves image quality and reduces noise.

### Filter with 3x3 Bilinear Filter

- Applies a 3x3 bilinear filter to blur the noisy image.
- Enhances image aesthetics by reducing high-frequency noise.

### De-noise with 3x3 Median Filter

- Utilizes a 3x3 median filter to remove noise from the image.
- Preserves edges while effectively reducing salt and pepper noise.

### De-noise with Gaussian Filter

- Applies a Gaussian filter with a specified sigma value (sigma = 1.5).
- Smoothens the image by convolving with a Gaussian kernel.

## Usage

1. Ensure you have OpenCV installed (`pip install opencv-python`).
2. Load your image by updating the file path in `cv.imread('img.png')`.
3. Adjust the `probability` parameter to control the density of salt and pepper noise.
4. Run the script to observe the visual results of various image processing operations.

```python
import cv2 as cv
import numpy as np
import random

