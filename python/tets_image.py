#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from PIL import Image, ImageDraw

img = Image.open('zophie.png')
print(img.size)
img.save('yy.jpg')

# 剪裁图片
croppedImg = img.crop((335, 345, 565, 560))
croppedImg.save('cropped.png')

# 拷贝copy()
# 粘贴paste()
# 调整大小resize()
# 旋转rotate()
# 翻转transpose()
# 获取或修改单个像素 getpixel()  setpixel()

im = Image.new('RGBA', (400, 400), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (399, 0), (399, 399), (0, 399), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 400, 10):
    draw.line([(i, 0), (400, i - 100)], fill='green')

draw.text((200,200),'Hello,every body!',fill='purple')
im.save('drawing.png')

# 点point()
# 线line()
# 矩形rectangle()
# 椭圆ellipse()
# 多边形polygon()
# 文本 text()
