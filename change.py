# 这个文件是在crossing那里copy过来的，用来做图像风格迁移，也先帖在这里

import cv2
net = cv2.dnn.readNetFromTorch('starry_night.t7')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV);
image = cv2.imread('mine3_change.jpg')
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
net.setInput(blob)
out = net.forward()
out = out.reshape(3, out.shape[2], out.shape[3])
out[0] += 103.939
out[1] += 116.779
out[2] += 123.68
out /= 255
out = out.transpose(1, 2, 0)
cv2.imshow('Styled image', out)
# cv2.imwrite('mine2_save.png', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
