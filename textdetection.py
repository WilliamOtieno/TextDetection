import cv2
import pytesseract

img = cv2.imread("image.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(pytesseract.image_to_string(img))
print(pytesseract.image_to_boxes(img))

cv2.imshow("Result", img)
cv2.waitKey(0)
