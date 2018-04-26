#!/usr/bin/python3

#sys系统命令行参数等
import sys
#操作系统的命令，例如mkdir,chown,getpid等
import os
#shell util,文件改名、移动
import shutil
#记录日志的工具
import logging
#粘贴板
import pyperclip
#浏览器
import webbrowser



logging.basicConfig(filename='log.out',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start of program')


print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\nPython 路径为：', sys.path, '\n')

#os.rmdir('yangyu')
#os.mkdir('yangyu')
#os.walk('yangyu')       #遍历目录
shutil.copy('baidu.html','./out')

#logging.disable(logging.CRITICAL)
logging.debug('end of program')

address= pyperclip.paste()
print(address)
webbrowser.open(address)