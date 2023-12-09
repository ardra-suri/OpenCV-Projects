import cv2 as cv
import numpy as np

# Convert to grayscale
image = cv.imread('Building.jpeg', cv.IMREAD_COLOR)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)
cv.waitKey(0)
cv.destroyAllWindows()


# Use the Canny edge detector. Set threshold values.
edges = cv.Canny(gray, 50, 150)
cv.imshow("Canny Edges", edges)
cv.waitKey(0)
cv.destroyAllWindows()

# Hough transform to detect lines 
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=10, maxLineGap=250)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
cv.imshow("Lines Detected", image)
cv.waitKey(0)
cv.destroyAllWindows()

# Implement a loop to increment the threshold and display lines for 3 different threshold values
for threshold in range(50, 250, 50):
    edges = cv.Canny(gray, threshold, threshold * 2)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=10, maxLineGap=250)
    result_image = image.copy()
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(result_image, (x1, y1), (x2, y2), (255, 0, 0), 3)
    cv.imshow(f"Lines with Threshold {threshold}", result_image)
    cv.waitKey(0)
cv.destroyAllWindows()

# e. Use the Hough transform to detect circles in the "Shapes" image and display them.
shapes_image = cv.imread('Shapes.jpg', cv.IMREAD_COLOR)
gray_shapes = cv.cvtColor(shapes_image, cv.COLOR_BGR2GRAY)
img_blur = cv.medianBlur(gray_shapes, 5)
height, width = gray_shapes.shape
circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, min(height, width) / 64, param1=200, param2=10, minRadius=5, maxRadius=30)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(shapes_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv.circle(shapes_image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv.imshow("Circles Detected", shapes_image)
cv.waitKey(0)
cv.destroyAllWindows()


if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(shapes_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv.circle(shapes_image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv.imshow("Circles Detected", shapes_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Implement a loop to vary minDist and maxRadius and display circles.
min_dists = [20, 40, 60]
max_radii = [20, 30, 40]

for min_dist, max_radius in zip(min_dists, max_radii):
    circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, min_dist, param1=200, param2=10, minRadius=5, maxRadius=max_radius)
    result_image = shapes_image.copy()
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv.circle(result_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv.circle(result_image, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv.imshow(f"Circles with MinDist {min_dist} and MaxRadius {max_radius}", result_image)
    cv.waitKey(0)
cv.destroyAllWindows()


