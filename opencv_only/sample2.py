# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("img/OpenCV.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色空間をBGRからグレースケールに変換

cv2.imshow("Gray Scale", gray)		# 名前が「Gray Scale」のウィンドウにimgを表示
cv2.waitKey(0)
cv2.destroyAllWindows()
