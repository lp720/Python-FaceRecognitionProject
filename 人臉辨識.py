import cv2 
img = cv2.imread('#photo path')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
facecascade = cv2.CascadeClassifier("#face_model.xml's path")
faceRect = facecascade.detectMultiScale(gray, 1.1, 4)
                                               #縮小倍率＃被匡到的次數
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(8000)