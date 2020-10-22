import sys, os

if __name__ == '__main__':

	foldersToSearch = []
	foldersToSearch.append('./')
	
	foundFiles = {}
	
	for currentFolder in foldersToSearch:
	
		listFilesDirectories = os.listdir(currentFolder)
	
		foldersToSearch.remove(currentFolder)
		
		for item in listFilesDirectories:
			if '.' in item:
				if item in foundFiles:
					print(currentFolder + item + ' : ' + str(foundFiles.get(item)))
				else:
					foundFiles[item] = currentFolder + item + '/'
			else:
				foldersToSearch.append(currentFolder + item + '/')
		