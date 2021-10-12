from PIL import Image
import cv2

img = cv2.imread('Database/1.jpg')
img = cv2.resize(img,(500,500))
img[20,40,0] = 36

cv2.imshow("hello",img)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() 
