# Optical Flow Visualization

This Python program captures video from the device's camera, calculates dense optical flow using the Farneback method, and visualizes the flow vectors. The optical flow vectors are displayed with color-coding to represent the direction and magnitude of motion. The program utilizes OpenCV and NumPy for image processing.

## Optical Flow Calculation and Visualization

1. **Video Capture Setup**
   - Starts a video capture using the device's camera (camera index `0`).
   - Checks if the video stream is opened successfully.

2. **Background Initialization**
   - Saves the first frame as the background for subsequent iterations.

3. **Optical Flow Computation**
   - Calculates dense optical flow between the background and the current frame using the Farneback method.

4. **Motion Thresholding**
   - Thresholds the optical flow magnitude to identify significant motion.

5. **Percentage of Significant Motion**
   - Calculates the percentage of pixels with significant motion.

6. **Optical Flow Visualization**
   - Converts the optical flow vectors into polar coordinates to obtain magnitude and angle.
   - Color-codes the vectors based on the direction of motion and displays the frame with optical flow vectors.

7. **Exit Conditions**
   - Press 'Q' or 'Esc' to exit the program.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python
