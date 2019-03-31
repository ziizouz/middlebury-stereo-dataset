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

# unzipping all downloaded file
# Getting all filenames
zip_names = glob.glob('*.zip')

for filename in zip_names:
	os.system('unzip ' + filename) # unzipping
	os.system('rm ' + filename) # removing zip file to save space
