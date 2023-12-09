# Precision-Recall Analysis

This Python program analyzes precision, recall, and F1 score based on Intersection over Union (IoU) values. The program calculates these metrics for different IoU thresholds and generates a Precision-Recall curve. It utilizes OpenCV, Matplotlib, NumPy, and Imutils for image processing and visualization.

## Precision, Recall, and F1 Calculation

1. **IOU Calculation and Analysis**
   - The `calculate_precision_recall_f1` function computes precision, recall, and F1 score based on IoU values.
   - Iterates over a range of IoU thresholds and prints the results for each threshold.

2. **Precision-Recall Curve**
   - Generates a Precision-Recall curve using Matplotlib.
   - Plots precision against recall for different IoU thresholds.

## Usage

1. Install the required libraries:
   ```bash
   pip install opencv-python matplotlib imutils
