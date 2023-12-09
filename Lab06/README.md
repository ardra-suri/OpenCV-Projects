# Image Template Matching

This Python program performs template matching between a query image and a template image using OpenCV. The template matching process involves resizing, rotating, and then matching the template to the query image. The program utilizes OpenCV and NumPy for image processing.

## Template Matching

1. **Load Images**
   - Reads the query image ('Trillium_s.jpg') and the template image ('Trillium_t.jpg').

2. **Image Size Check and Adjustment**
   - Ensures that the template image is smaller or equal in size to the query image.
   - Resizes the query image to double both width and height if needed.

3. **Image Rotation**
   - Rotates the query image by 30 degrees around its center using an affine transformation.

4. **Template Matching Algorithm**
   - Utilizes template matching with the specified method (`cv.TM_CCORR`).
   - The result of the template matching is stored in the `result` variable.

5. **Find Best Match Location**
   - Finds the location (top-left corner) of the best match in the result.

6. **Draw Rectangle Around Match**
   - Draws a rectangle around the identified match in the query image.

7. **Display Result**
   - Displays the query image with the rectangle around the matched region.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python
