import cv2

img = cv2.imread("img/OpenCV.png")	# �摜��ϐ�img�ɑ��

cv2.imshow("OpenCV", img)			# ���O���uOpenCV�v�̃E�B���h�E��img��\��
cv2.waitKey(0)						# �L�[���͑҂���Ԃ�����/���͂����L�[�͎w��Ȃ�
cv2.destroyAllWindows()				# ���ׂẴE�B���h�E�����

