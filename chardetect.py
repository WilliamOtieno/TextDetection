from textdetection import *

# Detecting Characters

hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for box in boxes.splitlines():
    box = box.split(" ")
    print(box)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
    cv2.putText(img, box[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
