import cv2
import math
import numpy as np
import random
# Importamos la imagen en formato
img0 = cv2.imread('mapa1.png')
# Leemos la imagen en binario

img = cv2.imread('mapa1.png',cv2.IMREAD_GRAYSCALE)
# Cambiamos el formato a RGB
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#Leemos la imagen en color gris
imgg = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
ret,imgb = cv2.threshold(imgg,127,255,cv2.THRESH_BINARY)

# Identificamos y dibujamos el cotorno de la pista
contours,hierarchy = cv2.findContours(imgb,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img0,contours,-1,(0,255,0),4)

number = 900
counter = 100
while counter > 0:
	counter-=1
	center_x = random.randint(0,number)
	center_y = random.randint(0,number)
	radius = random.randint(0,number/100)
	circle = cv2.circle(img0, (center_x, center_y), radius,(0,0,0), -1)

cv2.imshow("img",circle)
cv2.waitKey()
cv2.destroyAllWindows()


"""

def main():

    # 1. Create a white background image
    d = 400
    img = np.ones((d, d, 3), np.uint8) * 255

    # 2. Draw filled circles randomly in a loop
    for i in range(0, 100):
        # Random center point
        center_x = np.random.randint(0, high=d)
        center_y = np.random.randint(0, high=d)

        # Random radius and color
        radius = np.random.randint(5, high=d/5)
        color = np.random.randint(0, high=256, size=(3, )).tolist()

        cv2.circle(img, (center_x, center_y), radius, color, -1)

    # 3. Display the result
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
"""