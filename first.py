import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/girl.jpg")
imgresize = cv2.resize(img, (600, 400))
cv2.imshow("Image", imgresize)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()