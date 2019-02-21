#!/usr/local/bin/python3
# coding:utf-8
'''
二维码转字符串（URL）
'''
import sys
import os
import zxing
from PIL import Image

if __name__ == '__main__':
	argCount = len(sys.argv)
	#print(sys.argv)
	zxurl = ''
	if argCount < 2:
		print("请输入需要转换的图片名称")
	else:
		intputImageName = sys.argv[1]
		if  os.path.isfile(intputImageName):
			print('解析中，请稍等...')
			zx = zxing.BarCodeReader()
			zxurl = zx.decode(intputImageName)
			print("二维码图片是：%s \n解析结果是：%s"%(intputImageName,zxurl.parsed))
		elif os.path.exists(intputImageName):
			print("%s 是目录，请输入文件路径!"%intputImageName)
		else:
			print("文件不存在，请检查文件名："+intputImageName)
 


