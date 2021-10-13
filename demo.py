from PIL import Image
import cv2

img = cv2.imread('Database/1.jpg')
img = cv2.resize(img,(500,500))
img[499,1,0] = 3
img[40,20,0] = int("".join(str(i) for i in bin(img[40,20,0])[0] + bin(img[40,20,0])[2:-1] + '1'),2)
print(int("".join(str(i) for i in bin(img[40,20,0])[0] + bin(img[40,20,0])[2:-1] + '1'),2))

cv2.imshow("hello",img)
print(bin(img[499,1,0])[-1])
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() 
