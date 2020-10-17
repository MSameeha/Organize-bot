import os
import shutil
from os import listdir
from os.path import isfile, join

def file_organizer(mypath):
	files = [f for f in listdir(mypath) if isfile(join(mypath,f))]    #files in a given path
	file_type_variation_list=[] 									  #types of extension 
	filetype_folder_dict={}											  #files extensions for respective folders
	for file in files:
		filenamebrake = file.split('.')
		filetype=filenamebrake[len(filenamebrake)-1]
		if filetype not in file_type_variation_list:
			file_type_variation_list.append(filetype)
			new_folder_name = mypath + '/' + filetype + '_folder'
			filetype_folder_dict[str(filetype)] = str(new_folder_name)
			if os.path.isdir(new_folder_name) == True: #folder exists
				continue
			else:
				os.mkdir(new_folder_name)

	for file in files:
		src_path=mypath + '/' + file
		filenamebrake = file.split('.')
		filetype = filenamebrake[len(filenamebrake)-1]
		if filetype in filetype_folder_dict.keys():
			dest_path = filetype_folder_dict[str(filetype)]
			shutil.move(src_path,dest_path)
	print("File organization Completed " + str(mypath))

mypath = str(input("Enter Path "))
file_organizer(mypath)
