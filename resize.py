import cv2
import numpy as np

lamb_image = cv2.imread("lamb.jpeg")
pica_image = cv2.imread("pika.png")

cv2.imshow("Lamb images", lamb_image)
cv2.imshow("Pika images", pica_image)

#resizing the image 
resized_image = cv2.resize(lamb_image, (304,202))
cv2.imshow("Resized image", resized_image)

#erosion on the image 
#kernel is 2d list where every value has same value
kernel = np.ones((5,5), np.uint8)
eroded_image = cv2.erode(pica_image, kernel)
cv2.imshow("Eroded image", eroded_image)

cv2.waitKey()
cv2.destroyAllWindows()