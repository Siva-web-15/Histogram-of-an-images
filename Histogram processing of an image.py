# Developed By: Sivabalan M
# Register Number: 212224230269

import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("parrot.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist_original = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
equalized_image = cv2.equalizeHist(gray_image)
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plt.figure(figsize=(10, 7))
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
plt.subplot(2, 2, 3)
plt.plot(hist_original, color='black')
plt.title('Original Histogram')
plt.xlim([0, 256])
plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Equalized Histogram')
plt.xlim([0, 256])
plt.tight_layout()
plt.show()







