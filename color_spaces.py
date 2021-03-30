import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('Resources/Photos/park.jpg')
# plt.imshow(img);plt.show()

cv.imshow("Image",img)



#BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)


# BGR to l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("Lab",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow("RGB",rgb)
# we can also show with plt
# plt.imshow(rgb)
# plt.show()


# hsv to bgr
hsv_bgr =cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("Hst to bgr",hsv_bgr)



cv.waitKey(0)