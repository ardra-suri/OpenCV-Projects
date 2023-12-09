# Object Segmentation with Mask R-CNN

This Python program focuses on object segmentation using the Mask R-CNN (Region-based Convolutional Neural Network) model. It utilizes OpenCV and the pre-trained Mask R-CNN model to detect and segment objects in images.

## Segmentation Function

1. **Load Mask R-CNN Model**
   - Loads the Mask R-CNN model from the TensorFlow frozen graph and configuration files.

2. **Object Detection and Bounding Box Drawing**
   - Defines a function `detect_objects` to detect objects in an image and draw bounding boxes around them.

3. **Object Segmentation**
   - Defines a function `segment_objects` to segment objects in an image based on a given score threshold.
   - Applies the mask obtained from the model to segment the object.

4. **Image Loading and Processing**
   - Loads images ('Street.jpg' and 'WildLife.png').
   - Calls the `detect_objects` function to detect and draw bounding boxes for objects in the images.

5. **Display Results**
   - Displays the original images with bounding boxes drawn around detected objects.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python
