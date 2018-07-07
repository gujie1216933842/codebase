
import cv2

def cutting_img(im, im_position, img, xoffset=1, yoffset=1):
    filename = './out_img/' + img.split('.')[0]
    # 识别出的字符个数
    im_number = len(im_position[1])
    # 切割字符
    for i in range(im_number):
        im_start_X = im_position[1][i][0] - xoffset
        im_end_X = im_position[1][i][1] + xoffset
        im_start_Y = im_position[2][i][0] - yoffset
        im_end_Y = im_position[2][i][1] + yoffset
        cropped = im[im_start_Y:im_end_Y, im_start_X:im_end_X]
        cv2.imwrite(filename + '-cutting-' + str(i) + '.jpg', cropped)











        # 识别验证码
        cutting_img_num = 0
        for file in os.listdir('./out_img'):
            str_img = ''
            if fnmatch(file, '%s-cutting-*.jpg' % img_name.split('.')[0]):
                cutting_img_num += 1
        for i in range(cutting_img_num):
            try:
                file = './out_img/%s-cutting-%s.jpg' % (img_name.split('.')[0], i)
                # 识别字符
                str_img = str_img + image_to_string(Image.open(file), lang='eng', config='-psm 10')  # 单个字符是10，一行文本是7
            except Exception as err:
                pass
        print('切图：%s' % cutting_img_num)
        print('识别为：%s' % str_img)


def cutting_img(im, im_position, img, xoffset=1, yoffset=1):
    filename = './out_img/' + img.split('.')[0]
    # 识别出的字符个数
    im_number = len(im_position[1])
    # 切割字符
    for i in range(im_number):
        im_start_X = im_position[1][i][0] - xoffset
        im_end_X = im_position[1][i][1] + xoffset
        im_start_Y = im_position[2][i][0] - yoffset
        im_end_Y = im_position[2][i][1] + yoffset
        cropped = im[im_start_Y:im_end_Y, im_start_X:im_end_X]
        cv2.imwrite(filename + '-cutting-' + str(i) + '.jpg', cropped)
