import os
import glob
import cv2
import numpy as np

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
	os.system('rm ' + filename) # removing zip file to save space

# Converting PFM to PNG 
filenames = glob.glob('*-perfect') # All unzip filenames

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

