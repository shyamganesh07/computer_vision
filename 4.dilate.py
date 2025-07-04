import cv2
import numpy as np

# Step 1: Read the image in grayscale (dilation works on single channel)
image = cv2.imread('image.jpg', 0)

# Step 2: Define the kernel (matrix used for dilation)
kernel = np.ones((5, 5), np.uint8)  # You can change size (3x3, 7x7, etc.)

# Step 3: Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Step 4: Display original and dilated image
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
