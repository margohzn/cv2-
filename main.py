import cv2

#reading an image 
image = cv2.imread("opencv.png") #loading the image not displaying
#image2 = cv2.imread("/Users/margaret/Documents/coding_class/open_cv/opencv-assets-main/ghost.png") #loading image which is not in the same folder 

"""
image = cv2.imread("opencv.png", cv2.IMREAD_COLOR) #default color mode = cv2.IMREAD_COLOR
greyscale_image = cv2.imread("opencv.png", cv2.IMREAD_GRAYSCALE) #making color in black and white
unchanged_image = cv2.imread("opencv.png", cv2.IMREAD_UNCHANGED) #makes image brighter and more sharp 


#displaying the image 
cv2.imshow("Open cv logo", image)
cv2.imshow("Grey scale image", greyscale_image)
cv2.imshow("Un chnaged", unchanged_image)

#ssaving image 
cv2.imwrite("saved_grayscale_image.png", greyscale_image)
cv2.imwrite("/Users/margaret/Documents/coding_class/open_cv/opencv-assets-main/grey_opencv.png", greyscale_image)
"""

#splitting the image in red green blue saturations
blue, green, red, = cv2.split(image)

cv2.imshow("Open cv logo", image)
cv2.waitKey(delay = 5000)

cv2.imshow("blue saturation", blue)
cv2.waitKey(delay = 5000)

cv2.imshow("green saturation", green)
cv2.waitKey(delay = 5000)

cv2.imshow("red saturation", red)
cv2.waitKey(delay = 5000)


#hold window utill any keyboard key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows() #makes sure that when window is closed all infromation is deleted