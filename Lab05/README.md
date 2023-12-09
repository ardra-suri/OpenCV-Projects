# Image Processing: Edge and Circle Detection

This Python program focuses on edge detection using the Canny edge detector and line detection using the Hough transform. Additionally, it demonstrates circle detection in a separate image using the Hough Circle Transform. The program utilizes OpenCV and NumPy for efficient image processing.

## Edge Detection and Line Detection

1. **Convert to Grayscale**
   - Reads an image ('Building.jpeg') and converts it to grayscale.
   - Displays the grayscale image.

2. **Canny Edge Detection**
   - Applies the Canny edge detector to the grayscale image.
   - Displays the edges detected by Canny.

3. **Hough Transform for Line Detection**
   - Utilizes the Hough transform to detect lines in the image.
   - Displays the lines detected.

4. **Varying Thresholds for Line Detection**
   - Implements a loop to increment the Canny edge detection threshold.
   - Displays lines for three different threshold values.

## Circle Detection

5. **Hough Circle Transform**
   - Reads a separate image ('Shapes.jpg') and converts it to grayscale.
   - Applies the Hough Circle Transform to detect circles in the image.
   - Displays the circles detected.

6. **Varying Parameters for Circle Detection**
   - Implements a loop to vary minDist and maxRadius for circle detection.
   - Displays circles for different minDist and maxRadius values.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python
