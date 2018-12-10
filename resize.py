__author__ = 'BY'
from PIL import Image
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import imghdr

# def is_img(ext):
#     ext = ext.lower()
#     if ext == '.jpg':
#         return True
#     elif ext == '.png':
#         return True
#     elif ext == '.jpeg':
#         return True
#     elif ext == '.bmp':
#         return True
#     else:
#         return False

def get_name(path) :
    files = os.listdir(path)
    s = []
    for file in files:
        if not os.path.isdir(file) and imghdr.what(file):
            s.append(file)
    print(s)
    return s

def change_size(file,new_size):#改变图片分辨率
    try:
        n = 1
        for i in file:
            img = Image.open(i)
            size = img.size
            print('第{}张分辨率为{}'.format(n,[size]))

            if size[0] > size[1] :
                if new_size < size[0]:
                    print(new_size)
                    new_pic = img.resize((new_size, int(new_size/size[0]*size[1])), Image.ANTIALIAS)
                    new_pic.save('new_' + i)
                    print('修改后的照片分辨率为{}'.format(new_pic.size))
                if new_size > size[0]:
                    print('照片小于要修改的尺寸，无需修改')
                    pass

            elif size[0] < size[1] :
                if new_size < size[1]:
                    print(new_size)
                    new_pic = img.resize((int(new_size / size[1] * size[0]), new_size), Image.ANTIALIAS)
                    new_pic.save('new_' + i)
                    print('修改后的照片分辨率为{}'.format(new_pic.size))
                if new_size > size[0]:
                    print('照片小于要修改的尺寸，无需修改')
                    pass

    except Exception as  e:
        print(e)




if __name__ == '__main__':
    a = get_name('.')
    new_size = int(input('请输入要压缩的尺寸\n'))
    change_size(a,new_size)





