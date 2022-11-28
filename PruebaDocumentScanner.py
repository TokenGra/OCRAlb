import cv2
import numpy as np


'''image = cv2.imread("TestDoc2.jpg")  # read in the image
image = cv2.resize(image, (1300, 800))  # resizing because opencv does not work well with bigger images
orig = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # RGB To Gray Scale
cv2.imshow("Title", gray)

blurred = cv2.GaussianBlur(gray, (5, 5),
                           0)  # (5,5) is the kernel size and 0 is sigma that determines the amount of blur
cv2.imshow("Blur", blurred)

edged = cv2.Canny(blurred, 30, 50)  # 30 MinThreshold and 50 is the MaxThreshold
cv2.imshow("Canny", edged)

kernel = np.ones((7,7), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

area_thresh = 0

# the loop extracts the boundary contours of the page
for c in contours:
    area = cv2.contourArea(c)
    if area > area_thresh:
        area_thresh = area
        big_contour = c

approx = mapper.mapp(big_contour)  # find endpoints of the sheet

pts = np.array([[0, 0], [800, 0], [800, 800], [0, 800]], np.float32)  # map to 800*800 target window

op = cv2.getPerspectiveTransform(approx, pts)  # get the top or bird eye view effect
dst = cv2.warpPerspective(orig, op, (800, 800))

cv2.imshow("Scanned", dst)
# press q or Esc to close
cv2.waitKey(0)
cv2.destroyAllWindows()


'''

