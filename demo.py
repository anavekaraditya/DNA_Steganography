from PIL import Image
import cv2

img = cv2.imread('we1.jpg')
print(img.shape)
#img[100:120,100,0] = 48
#cv2.imwrite('we1.jpg',img)
print(img[100,100,0])
cv2.imshow("hello",img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()

