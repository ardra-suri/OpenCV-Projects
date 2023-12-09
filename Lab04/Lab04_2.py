import cv2 as cv
import numpy as np
import random

image = cv.imread('img.png')

# Add salt and pepper noise
def add_salt_and_pepper_noise(image, probability):
    noisy_image = np.copy(image)
    num_pixels = int(probability * image.shape[0] * image.shape[1])
    for _ in range(num_pixels):
        row, col = random.randint(0, image.shape[0] - 1), random.randint(0, image.shape[1] - 1)
        if random.random() < 0.5:
            noisy_image[row, col] = [0, 0, 0]  # Black pepper noise
        else:
            noisy_image[row, col] = [255, 255, 255]  # White salt noise
    return noisy_image

probability = 0.25  
noisy_image = add_salt_and_pepper_noise(image, probability)

# Display
cv.imshow('Noisy Image', noisy_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Smooth with 3x3 box-kernel
kernel = np.ones((3, 3), np.float32) / 9
smoothed_image = cv.filter2D(noisy_image, -1, kernel)

# Display 
cv.imshow('Smoothed Image', smoothed_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Filter with 3x3 bilinear filter 
blurred_image = cv.GaussianBlur(noisy_image, (3, 3), 0)

# Choose the central pixel coordinates (i, j)
i, j = 4, 4  # Adjust these coordinates as needed

# Get the pixel values for the central pixel and its neighbors in the original noisy image
center_pixel_value = noisy_image[i, j][0]
neighbor_sum = np.sum(noisy_image[i-1:i+2, j-1:j+2, 0])

# Calculate the expected value for the central pixel in the blurred image
expected_value = (center_pixel_value + neighbor_sum) / 9

# Get the actual value for the central pixel in the blurred image
actual_value = blurred_image[i, j][0]

# Print the results
print(f"Central Pixel (i, j): ({i}, {j})")
print(f"Central Pixel Blue Value (Original): {center_pixel_value}")
print(f"Sum of Neighbor Blue Values (Original): {neighbor_sum}")
print(f"Expected Central Pixel Value (Blurred): {expected_value}")
print(f"Actual Central Pixel Value (Blurred): {actual_value}")



# Display 
cv.imshow('Blurred Image', blurred_image)
cv.waitKey(0)
cv.destroyAllWindows()

# De-noise with x3 median filter
median_filtered_image = cv.medianBlur(noisy_image, 3)

# Display 
cv.imshow('Median-Filtered Image', median_filtered_image)
cv.waitKey(0)
cv.destroyAllWindows()

# De-noise with a Gaussian filter with sigma = 1.5
sigma = 1.5
gaussian_filtered_image = cv.GaussianBlur(noisy_image, (3, 3), sigma)

# Display 
cv.imshow('Gaussian Filtered Image', gaussian_filtered_image)
cv.waitKey(0)
cv.destroyAllWindows()



