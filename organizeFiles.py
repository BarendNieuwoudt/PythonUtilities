# python organizeFiles.py <starting directory> <file name regex> <destination directory>
# for example: python organizeFiles.py ./ *.txt ./SomeTextFiles
# moves files in the current directory, matching the regex into the specified directory

import glob, sys, os

def move(location, file, newFolder):
	
	if len(glob.glob(newFolder)) == 0:
		# Destination Directory does not exist, create it
		os.mkdir(newFolder)
		
	# Get all the files matching the regex
	files = glob.glob(location + file)
	
	for x in files:
		# Add files to Destination Directory
		os.rename(x, newFolder + x)
		
if __name__ == "__main__":
	move(sys.argv[1], sys.argv[2], sys.argv[3])
