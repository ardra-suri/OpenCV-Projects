import csv
import cv2 as cv
import matplotlib.pyplot as plt
import imutils
import numpy as np

def calculate_precision_recall_f1(iou_list, num_face_files, threshold):
    true_positives = 0
    false_positives = 0
    false_negatives = num_face_files

    for iou in iou_list:
        if iou >= threshold:
            true_positives += 1
            false_negatives -= 1
        else:
            false_positives += 1

    if true_positives == 0:
        precision = 0
        recall = 0
        f1 = 0
    else:
        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1 = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1

iou_thresholds = np.arange(0, 1, 0.1)

for threshold in iou_thresholds:
    precision, recall, f1 = calculate_precision_recall_f1(iou_list, num_face_files=8, threshold=threshold)
    print(f"Threshold: {threshold:.1f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1: {f1:.2f}")
    print()

precisions = []
recalls = []

for threshold in iou_thresholds:
    precision, recall, _ = calculate_precision_recall_f1(iou_list, num_face_files=8, threshold=threshold)
    precisions.append(precision)
    recalls.append(recall)

plt.plot(recalls, precisions, marker='o', linestyle='-')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.grid(True)
plt.show()