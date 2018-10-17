import cv2

img = cv2.imread('girl.jpg') # , cv2.IMREAD_GRAYSCALE
# cv2.namedWindow("image") # , cv2.WINDOW_NORMAL
img_copy = img.copy()

shape_num = img.shape # 这里元组的三个参数——（高，宽，通道）

start_height = int(shape_num[0]*0.8)
start_width = int(shape_num[1]*0.4)

print(start_height, start_width)

font = cv2.FONT_HERSHEY_SIMPLEX
img_write = cv2.putText(img, '000', (start_width, start_height), font, 1.2, (45, 122, 23), 2) #这里的参数先宽后高

cv2.imshow('image', img)
cv2.imshow('write', img_write)
cv2.imshow('copy', img_copy)
# print(shape_num)
#change_width = shape_num[0]*0.5
#change_height = shape_num[1]*0.5

#change_width = int(change_width)
#change_height = int(change_height)

#res = cv2.resize(img, (change_height, change_width), interpolation=cv2.INTER_AREA) # 这里传入的参数需要是整数
#cv2.imwrite('girl.jpg', res)

# cv2.putText('page4_19.jpg', 'abc', (600,400), 'r')
#cv2.imshow('image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
