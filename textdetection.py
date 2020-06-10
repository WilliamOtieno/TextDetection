import cv2
import pytesseract

img = cv2.imread("test.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detecting Words

hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)
for x, box in enumerate(boxes.splitlines()):
    if x != 0:
        box = box.split()
        print(box)
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
