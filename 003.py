__author__ = 'BY'
from PIL import Image,ImageDraw
import PIL
import os
import sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def get_name(file) :
    name = os.listdir(file)
    return name

def change_size(file):#改变图片分辨率
    name = get_name(file)
    for i in range(0,len(name)):
        photo_name = file + '/' + name[i]
        print(photo_name)
        img = Image.open(photo_name)
        new_size = img.size
        if new_size[0] > 640 and new_size[1] > 1136:
            new_pic = img.resize((640,1136),Image.ANTIALIAS)
        if new_size[0] > 640 and new_size[1] < 1136:
            new_pic = img.resize((640,new_size[1]),Image.ANTIALIAS)
        if new_size[0] < 640 and new_size[1] > 1136:
            new_pic = img.resize((new_size[0],1136),Image.ANTIALIAS)
        if new_size[0] < 640 and new_size[1] < 1136:
            new_pic = img.resize((new_size[0],new_size[1]),Image.ANTIALIAS)
        new_pic.save('photo2'+'/'+name[i])
        new_pic.close()
        img2 = Image.open('photo2'+'/'+name[i])
        print(img2.size)
        img2.close




if __name__ == '__main__':
    x = change_size('photo')
    sys.exit("bye")
    #print(help(Image))
    #x = (320,480)
    #print(x[0])




