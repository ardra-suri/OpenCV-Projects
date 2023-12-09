import cv2 as cv
import numpy as np
import time

# Start a video capture, using device's camera
cap = cv.VideoCapture(0)

# Check if video file opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
total_pixels = frame_width * frame_height

first_frame_flag = True

# Read until the video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert captured frames to grayscale
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Save the first frame as the background
    if first_frame_flag:
        background = gray_frame
        first_frame_flag = False

    # Calculate dense optical flow using Farneback method
    flow = cv.calcOpticalFlowFarneback(background, gray_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Convert optical flow into Polar coordinates to get magnitude
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])

    # Use a threshold to only count the significant ones
    mag_thresholded = (mag > 20)

    # Calculate the percentage of significant motion
    percent = mag_thresholded.sum() / total_pixels

    # Display the optical flow vectors
    hsv = np.zeros_like(frame)
    hsv[..., 1] = 255

    # Use color to represent the direction of motion
    ang_degrees = ang * 180 / np.pi / 2
    hsv[..., 0] = ang_degrees
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

    # Convert HSV to BGR for visualization
    flow_rgb = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    # Display the frame with optical flow vectors
    cv.imshow('Optical Flow', flow_rgb)

    # Press Q on keyboard to exit
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break

    # Press ESC on keyboard to exit
    if key & 0xFF == 27:
        break

    # Update the background for the next iteration
    background = gray_frame

# Release the video capture
cap.release()

# Close all the frames
cv.destroyAllWindows()
