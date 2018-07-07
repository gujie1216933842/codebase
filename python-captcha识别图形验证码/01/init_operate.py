import cv2

# 自适应阀值二值化
def _get_dynamic_binary_image(filedir, img_name):
  filename =   './out_img/' + img_name.split('.')[0] + '-binary.jpg'
  img_name = filedir + '/' + img_name
  print('.....' + img_name)
  im = cv2.imread(img_name)
  im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #灰值化
  # 二值化
  th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
  cv2.imwrite(filename,th1)
  return th1



# 去除边框
def clear_border(img,img_name):
  filename = './out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
  h, w = img.shape[:2]
  for y in range(0, w):
    for x in range(0, h):
      if y < 2 or y > w - 2:
        img[x, y] = 255
      if x < 2 or x > h -2:
        img[x, y] = 255

  cv2.imwrite(filename,img)
  return img