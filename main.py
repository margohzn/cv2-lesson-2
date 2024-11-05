import cv2 

dog_image = cv2.imread("dog.jpg")
rabbit_image = cv2.imread("rabbit.jpg")

cv2.imshow("Dog image", dog_image)
cv2.imshow("Rabbit image", rabbit_image)

# apply arithmetic operation,  directly subtracting or adding pixle value 
# only works if both imgaes have same size (dimension) and same image format 

#addition of images
weighted_sum = cv2.addWeighted(dog_image, 0.5, rabbit_image, 0.4, 0)
cv2.imshow("Addition of pixels", weighted_sum)

#subtraction of images 
weighted_sub = cv2.subtract(rabbit_image, dog_image)
cv2.imshow("Subtraction of pixels", weighted_sub)



cv2.waitKey(0)
cv2.destroyAllWindows()