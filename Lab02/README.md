# Real-Time Video Capture and Snapshot

This Python program captures real-time video from the device's camera using OpenCV and allows users to take snapshots by pressing the 'x' key. The captured frames are displayed, and snapshots are saved with an automatically incremented filename. 

## Features

- Real-time video capture from the device's camera.
- Press 'x' to take a snapshot.
- Snapshots are saved with an automatically incremented filename.
- The snapshot is cropped by removing 30 pixels from each side.
- A constant border, 50 pixels wide, is added to the snapshot.
- Snapshots are saved as 'imageX.jpg', where X is an automatically incremented counter.
- Display the captured video and snapshots.
- Press 'q' or 'ESC' to exit the video capture.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python
