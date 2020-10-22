# This python script will search through all the files and print the duplicates

import sys, os

if __name__ == '__main__':

	foldersToSearch = []
	
	# Start with searching the current folder
	foldersToSearch.append('./')
	
	foundFiles = {}
	
	for currentFolder in foldersToSearch:
	
		# Return all the files/folders in the currently searched directory
		listFilesDirectories = os.listdir(currentFolder)
	
		# Once a folder has been searched, it can be removed
		foldersToSearch.remove(currentFolder)
		
		for item in listFilesDirectories:
			if '.' in item:
				# Files have extentions
				if item in foundFiles:
					# This file name has been found before, print both locations
					print(currentFolder + item + ' : ' + str(foundFiles.get(item)))
				else:
					foundFiles[item] = currentFolder + item + '/'
			else:
				# This item is a directory, add it to be searched
				foldersToSearch.append(currentFolder + item + '/')
		
