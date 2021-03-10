import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('avatar1.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(np.concatenate((image,image)))
plt.show()