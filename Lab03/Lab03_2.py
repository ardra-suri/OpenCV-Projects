import numpy as np
import cv2 as cv

drawing = False  # True if mouse is pressed
mode = 'rectangle'  # 'rectangle', 'circle', or 'polyline'
ix, iy = -1, -1
color = (0, 0, 255)  # Default drawing color is red (0, 0, 255)

# Create a black image to start with
img = np.zeros((512, 512, 3), np.uint8)

# Mouse callback function
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, color, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode == 'rectangle':
                cv.rectangle(img, (ix, iy), (x, y), color, -1)
            elif mode == 'circle':
                cv.circle(img, (x, y), 5, color, -1)
            elif mode == 'polyline':
                # Implement polyline drawing logic here
                cv.line(img, (ix, iy), (x, y), color, 2, cv.LINE_AA)
                ix, iy = x, y  # Update the starting point for the next segment
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'rectangle':
            cv.rectangle(img, (ix, iy), (x, y), color, -1)
        elif mode == 'circle':
            cv.circle(img, (x, y), 5, color, -1)

# Function to change drawing color based on user input
def change_color(key):
    global color
    if key == ord('r'):
        color = (0, 0, 255)  # Red
    elif key == ord('w'):
        color = (255, 255, 255)  # White
    elif key == ord('g'):
        color = (0, 255, 0)  # Green
    elif key == ord('y'):
        color = (0, 255, 255)  # Yellow

cv.namedWindow('image')
cv.setMouseCallback('image', draw_shape)  # Use the draw_shape callback for drawing rectangles, circles, and polylines

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        if mode == 'rectangle':
            mode = 'circle'
        elif mode == 'circle':
            mode = 'polyline'
        else:
            mode = 'rectangle'
    elif k == ord('r') or k == ord('w') or k == ord('g') or k == ord('y'):
        change_color(k)
    elif k == ord('l'):
        # Load a new image (or use a black image)
        img = np.zeros((512, 512, 3), np.uint8)
    elif k == ord('x'):
        # Save the image when 'x' is pressed
        cv.imwrite('drawn_image.png', img)
    elif k == 27:
        break

cv.destroyAllWindows()
