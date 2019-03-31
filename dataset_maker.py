import os
import glob
import cv2
import numpy as np
import pickle

# Read links from txt file
links_file_name = "dataset_links.txt"


# Download all selected links to local drive
with open(links_file_name, 'r') as links_file:
	
	link = links_file.readline()
	
	while link:
		print(link)
		# download file 
		ret = os.system('wget -c ' + link)
		if ret == 0:
			link = links_file.readline()

# unzipping all downloaded file
# Getting all filenames
zip_names = glob.glob('*.zip')

for filename in zip_names:
	os.system('unzip ' + filename) # unzipping
	#os.system('rm ' + filename) # removing zip file to save space

# Converting PFM to PNG 
filenames = glob.glob('*-perfect') # All unzip filenames
print(filenames)
for filename in filenames:

	# Removing -sd.pfm since I am not interested in those
	sd_pfm_files = glob.glob(filename + '/*-sd.pfm')
	for sd_pfm_file in sd_pfm_files:
		os.system('rm ' + sd_pfm_file)

	# Converting PFM to PNG
	pfm_files = glob.glob(filename + '/*.pfm')
	for pfm_file in pfm_files:
		png_filename = pfm_file[:-4] # removing .pfm to be replaced by PNG
		os.system('convert ' + pfm_file + ' ' + png_filename + '.png')
		os.system('rm ' + pfm_file)

	# removing pgm files since I am not interested in those
	pgm_files = glob.glob(filename + '/*.pgm')
	for pgm_file in pgm_files:
		os.system('rm ' + pgm_file)
	# removing lightning images (E & L) since I am not interested in those
	lightning_file = glob.glob(filename + '/*1L.png')
	os.system('rm ' + lightning_file[0])
	lightning_file = glob.glob(filename + '/*1E.png')
	os.system('rm ' + lightning_file[0])

## Creation of the pickle
depth_imgs = []
gray_imgs  = []

for filename in filenames:
	png_depth_files = glob.glob(filename + '/disp*.png')
	png_im_files = glob.glob(filename + '/im*.png')
	for png_depth_file, png_im_file  in zip(png_depth_files, png_im_files):
		# Adding depth file
		depth = cv2.imread(png_depth_file, 0) # read as gray img
		depth_imgs.append(depth)
		# Adding im file as gray
		im = cv2.imread(png_im_file, 0) # read as gray image
		gray_imgs.append(im)

# File lists are ready, let's save them into a pickle
# Saving depth images
with open('depth.pickle', "wb") as pickle_out:
	pickle.dump(depth_imgs, pickle_out)

# Saving gray images
with open('gray.pickle', "wb") as pickle_out:
	pickle.dump(gray_imgs, pickle_out)

# Done