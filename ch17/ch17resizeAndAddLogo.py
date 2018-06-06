#! python3
# -*- coding: utf-8 -*-
# @date: 2018/6/6 21:27
# @name: ch17
# @author：Go361
# resizeAndAddLogo.py - Resize all images in current working directory to fit
# in a 1500x1500 square, and adds zophie.png to the lower-right corner.

import os, re
from PIL import Image

SQUARE_FIT_SIZE = 1500
LOGO_FILENAME = 'zophie.png'

## 创建目标文件夹
dstDir = os.path.join(os.getcwd(), 'withLogo')
if not os.path.exists(dstDir):
	os.mkdir(dstDir)

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# TODO: Loop over all files in the working directory
Regex = re.compile(r'.jpg|.png|.gif|.bmp', re.IGNORECASE)
# print(os.listdir('.'))
for filename in os.listdir('.'):
	print(filename)
	if filename == LOGO_FILENAME:
		continue	# skip the logo file itself
	elif not Regex.search(filename[-4:]):
		continue	# skip non-image files
	im = Image.open(filename)
	width, height = im.size
	# skip too small photos
	if width < SQUARE_FIT_SIZE and height < SQUARE_FIT_SIZE:
		continue
	# Check if image needs to be resized

	#Calculate the new width and height to resize to.
	else:
		if width > height:
			height = int((SQUARE_FIT_SIZE / width) * height)
			width = SQUARE_FIT_SIZE
		else:
			width = int((SQUARE_FIT_SIZE / height) * width)
			height = SQUARE_FIT_SIZE
		# Resize the image.
		print("Resizing %s..." %(filename))
		im = im.resize((width, height))

	# Add the logo.
	print("Adding logo to %s" %(filename))
	im.paste(logoIm, (width - logoWidth, height - logoHeight))
	# Save changes.
	print(os.path.join(os.getcwd(), 'withLogo'))
	im.save(os.path.join(dstDir, filename))

