from textdetection import *

# Detecting Digits

hImg, wImg, _ = img.shape
config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config=config)
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
