# Interactive Drawing Tool

This Python program is an interactive drawing tool that allows users to create simple drawings on a canvas using rectangles, circles, and polylines. It utilizes the OpenCV and NumPy libraries for image processing and manipulation.

## Features

### Drawing Shapes

- Press and hold the left mouse button to start drawing.
- Choose the drawing mode ('rectangle', 'circle', or 'polyline') using the 'm' key.
- Release the mouse button to stop drawing.

### Change Drawing Color

- Press 'r' for red, 'w' for white, 'g' for green, and 'y' for yellow.

### Change Drawing Mode

- Press the 'm' key to cycle through drawing modes: rectangle, circle, and polyline.

### Clear Canvas

- Press 'l' to load a new image (or use a black image).

### Save Drawing

- Press 'x' to save the current drawing as 'drawn_image.png'.

### Exit Program

- Press the 'Esc' key (27) to exit the program.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python
