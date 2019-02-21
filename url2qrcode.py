#!/usr/local/bin/python3
# coding:utf-8
'''
字符串（URL）转二维码
'''
import sys
import os
import qrcode
import hashlib


if __name__ == '__main__':
	argCount = len(sys.argv)
	#print(sys.argv)
	if argCount < 2:
		print("请输入需要转换的url")
	else:
		intputurl = sys.argv[1]

		#imageName (url -> md5)
		m = hashlib.md5()
		urlencode = intputurl.encode(encoding='UTF-8')
		m.update(urlencode)
		imageName = m.hexdigest() + '.png'
		#print('imageName:'+imageName)
		#print('intputurl:'+intputurl)

		#image
		#qrCode = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)
		image = qrcode.make(intputurl)
		with open(imageName,'wb') as f:
			image.save(f)


		print("输入url是%s,生成二维码是%s"%(intputurl,imageName))

		# 显示二维码图片
		os.system('imgcat %s'%imageName)


		#inputy = input('是否打开图片目录？（y/n）')

		#if inputy == 'y':
			# 打开当前目录
			#os.system('open ./')
			


