#! python3
# -*- coding: utf-8 -*-
# @date: 2018/6/11 12:02
# @name: ch17recognizePhotoDir
# @author：Go361

# Import modules and write comments to describe this program.
import os,re
from PIL import Image

Regex = re.compile(r'.jpg|.png', re.IGNORECASE)

for dirpath, dirnames, filenames in os.walk('D:\\'):
	numPhotoFiles = 0
	numNonPhotoFiles = 0
	for filename in filenames:
		## Check if file extension isn't .png or .jpg.
		isPhoto = Regex.search(filename[-4:])
		if not isPhoto:
			numNonPhotoFiles += 1
			continue # skip to next filename
		## Open image file using Pillow.
		im = Image.open(os.path.join(dirpath, filename))
		width, height = im.size
		# print(filename, width, height)
		## Check if width & height are larger than 500.
		if width >500 and height > 500:
			## Image is large enough to be considered a photo.
			numPhotoFiles += 1
		else:
			## Image is too small to be a photo.
			numNonPhotoFiles += 1
		## If more than half of files were photos, print the absolute path of the folder.
	if numNonPhotoFiles < numPhotoFiles:
		print("The Folder ' %s ' is a Photo Folder " % dirpath)