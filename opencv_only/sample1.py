# -*- coding: utf-8 -*-
import cv2

img = cv2.imread("img/OpenCV.png")	# 画像を変数imgに代入

cv2.imshow("OpenCV", img)		# 名前が「OpenCV」のウィンドウにimgを表示
cv2.waitKey(0)				# キー入力待ち状態を示す/入力されるキーは指定なし
cv2.destroyAllWindows()			# すべてのウィンドウを閉じる
