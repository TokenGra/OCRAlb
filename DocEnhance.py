import cv2
import numpy as np

'''Read the image
Find the contours
Select the one with maximum area, ( and also somewhat equivalent to square).
Find the corner points.'''


# Leer imagen y resize
def GetImage(img):
    img = cv2.resize(img, [2000, 2000])
    ConversionsWhile(img)


def ConversionsWhile(img):
    # Convertir a Gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = np.zeros(gray.shape, np.uint8)
    # blur imagen
    clahe = cv2.createCLAHE(clipLimit=5)
    final_img = clahe.apply(gray)
    thresh = cv2.threshold(final_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    contour, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    best_cnt = None
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area > 1000:
            if area > max_area:
                max_area = area
                best_cnt = cnt

    # Delinea contorno en la mascara
    cv2.drawContours(mask, [best_cnt], 0, 255, -1)
    cv2.drawContours(mask, [best_cnt], 0, 0, 2)

    # Imagen con mascara aplicada
    res = cv2.bitwise_and(thresh, thresh, mask=mask)

    cv2.addWeighted(res, 1.5, res, -0.5, 0, res);

    peri = cv2.arcLength(best_cnt, True)

    try:
        # LA LINEA PROBLEMATICA
        corners = (cv2.approxPolyDP(best_cnt, 0.04 * peri, True)).reshape(4, 2)

        # cv2.drawContours(res, [best_cnt], -1, (0,0,255), 1, cv2.LINE_AA)

        # Perspective transform

        # Here, I have used L2 norm. You can use L1 also.
        width_AD = np.sqrt(((corners[0][0] - corners[3][0]) ** 2) + ((corners[0][1] - corners[3][1]) ** 2))
        width_BC = np.sqrt(((corners[1][0] - corners[2][0]) ** 2) + ((corners[1][1] - corners[2][1]) ** 2))
        maxWidth = max(int(width_AD), int(width_BC))

        height_AB = np.sqrt(((corners[0][0] - corners[1][0]) ** 2) + ((corners[0][1] - corners[1][1]) ** 2))
        height_CD = np.sqrt(((corners[2][0] - corners[3][0]) ** 2) + ((corners[2][1] - corners[3][1]) ** 2))
        maxHeight = max(int(height_AB), int(height_CD))

        output_pts = np.float32([[0, 0],
                                 [0, maxHeight - 1],
                                 [maxWidth - 1, maxHeight - 1],
                                 [maxWidth - 1, 0]])
        input_pts = np.float32([corners[0], corners[1], corners[2], corners[3]])
        M = cv2.getPerspectiveTransform(input_pts, output_pts)
        trans_img = cv2.warpPerspective(res, M, [maxWidth, maxHeight], flags=cv2.INTER_LINEAR)

        # Mostrar imagenes
        # cv2.imshow('Imagen', img)
        # cv2.imshow('Gris', res)
        # cv2.imshow('Grisd', mask)
        cv2.imshow('', trans_img)
        '''kernel = np.ones((1, 1), np.uint8)
        trans_img = cv2.erode(trans_img, kernel)'''

        res = cv2.resize(res, [1000, 1000])
        return res
    except Exception as e:
        print(f'Error : {e}')
        if res is not None:
            return res
