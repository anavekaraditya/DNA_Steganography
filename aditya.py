import cv2

original = cv2.imread("E:/5th Sem/E1-DWS/project/Database/2.jpg")
n = original.shape
print((n[0]*n[1]*n[2])/2)