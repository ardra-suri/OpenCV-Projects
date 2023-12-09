import cv2
import numpy as np

# Load the Mask R-CNN model
net = cv2.dnn.readNetFromTensorflow("frozen_inference_graph.pb", "mask_rcnn_inception_v2_coco_2018_01_28.pbtxt")

# Function to segment objects with different scores
def segment_objects(image, score_threshold):
    height, width, _ = image.shape

    # Prepare the image for the model
    blob = cv2.dnn.blobFromImage(image, swapRB=True)
    net.setInput(blob)

    # Get output from the Mask R-CNN
    boxes, masks = net.forward(["detection_out_final", "detection_masks"])
    detection_count = boxes.shape[2]

    # Segment objects with the given score threshold
    for i in range(detection_count):
        box = boxes[0, 0, i]
        class_id = int(box[1])
        score = box[2]

        if score > score_threshold:
            mask = masks[i, class_id]
            mask = cv2.resize(mask, (width, height))

            # Threshold the mask values to create a binary mask
            _, mask = cv2.threshold(mask, 0.5, 255, cv2.THRESH_BINARY)

            # Ensure the mask is of type CV_8U
            mask = mask.astype(np.uint8)

            # Apply the mask to the image
            segmented_object = cv2.bitwise_and(image, image, mask=mask)

            cv2.imshow(f"Segmentation (Score: {score})", segmented_object)
            cv2.waitKey(0)

# Load images
street_image = cv2.imread("Street.jpg")
wildlife_image = cv2.imread("WildLife.png")

# Segment objects in Street image
segment_objects(street_image.copy(), score_threshold=0.5)

# Segment objects in Wildlife image
segment_objects(wildlife_image.copy(), score_threshold=0.5)

cv2.destroyAllWindows()
