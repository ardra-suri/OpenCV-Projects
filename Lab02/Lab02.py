import cv2 as cv
import numpy as np

# Start a video capture, using device's camera
cap = cv.VideoCapture(0)

# Check if video file opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Printing width and height of video capture
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print("Frame width: ", frame_width)
print("Frame height: ", frame_height)

# Counter for naming the saved images
counter = 0

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        break

    # Display the frame
    cv.imshow('frame', frame)
    key = cv.waitKey(1)

    # Press 'q' or 'ESC' on keyboard to exit
    if key & 0xFF == ord('q') or key == 27:
        break

    #'x' key to take a snapshot
    if key == ord('x'):
        # Crop 30 pixels around the snapshot image
        cropped_frame = frame[30:-30, 30:-30]

        # Pad it with a constant border 50 pixels wide 
        borderColor = [137, 207, 240] 
        borderedImg = cv.copyMakeBorder(cropped_frame, 50, 50, 50, 50, cv.BORDER_CONSTANT, value=borderColor)

        # Save the snapshot with an automatically incremented filename
        counter += 1
        imageName = f'image{counter}.jpg'
        cv.imwrite(imageName, borderedImg)

        # Show the image in a new window for 1 second
        cv.imshow('snapshot', borderedImg)
        cv.waitKey(1000)
        cv.destroyWindow('snapshot')

# Release the video capture
cap.release()

# Close all the frames
cv.destroyAllWindows()
