import cv2 as cv
import numpy as np

# Load images
query_image = cv.imread('Trillium_s.jpg')
template_image = cv.imread('Trillium_t.jpg')

# Ensure that the template image is smaller or equal in size to the query image
if template_image.shape[0] > query_image.shape[0] or template_image.shape[1] > query_image.shape[1]:
    raise ValueError("Template image is larger than the query image")

# Resize the query image to double both width and height
query_image = cv.resize(query_image, (query_image.shape[1] * 2, query_image.shape[0] * 2))

# Rotate the query image by 30 degrees around the center
height, width = query_image.shape[:2]
center = (width // 2, height // 2)
rotation_matrix = cv.getRotationMatrix2D(center, 30, 1)
query_image = cv.warpAffine(query_image, rotation_matrix, (width, height))

# Template matching 
# result = cv.matchTemplate(query_image, template_image, cv.TM_SQDIFF)
result = cv.matchTemplate(query_image, template_image, cv.TM_CCORR)


# Find location 
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# Get the dimensions of the template image
template_width, template_height = template_image.shape[1], template_image.shape[0]

# Draw a rectangle around the best match
top_left = min_loc
bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
cv.rectangle(query_image, top_left, bottom_right, (0, 255, 0), 2)

cv.imshow('Matching Result', query_image)
cv.waitKey(0)
cv.destroyAllWindows()
