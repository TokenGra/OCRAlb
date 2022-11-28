import cv2
import numpy as np

'''Read the image
Find the contours
Select the one with maximum area, ( and also somewhat equivalent to square).
Find the corner points.'''

#Leer imagen y resize
img = cv2.imread('Test3.jpg')
img = cv2.resize(img,[700,700])

#Convertir a Gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = np.zeros((gray.shape),np.uint8)
# blur imagen
blur = cv2.GaussianBlur(gray, (3,3), 0)

thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
contour,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
best_cnt = None
for cnt in contour:
    area = cv2.contourArea(cnt)
    if area > 1000:
        if area > max_area:
            max_area = area
            best_cnt = cnt

#Delinea contorno en la mascara
cv2.drawContours(mask,[best_cnt],0,255,-1)
cv2.drawContours(mask,[best_cnt],0,0,2)

#Imagen con mascara aplicada
res = cv2.bitwise_and(img,img,mask = mask)

peri = cv2.arcLength(best_cnt, True)
corners = cv2.approxPolyDP(best_cnt, 0.04 * peri, True)

cv2.drawContours(res, contour, -1, (0,0,255), 1, cv2.LINE_AA)

#Mostrar imagenes
cv2.imshow('Imagen', img)
cv2.imshow('Gris', res)
cv2.imshow('Grisd', mask)


'''
cv2.imshow('Imagen',img)
cv2.imshow('Imagen',img)
cv2.imshow('Imagen',img)'''

cv2.waitKey(0)