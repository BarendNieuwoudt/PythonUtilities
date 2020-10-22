# python organizeFiles.py ./ *.psd ./STUFFHERE
# moves files in the current directory, ending on .psd into a STUFFHERE folder

import glob, sys, os

def move(location, file, newFolder):
	if len(glob.glob(newFolder)) == 0:
		os.mkdir(newFolder)
	files = glob.glob(location + file)
	for x in files:
		os.rename(x, newFolder + x)
		
if __name__ == "__main__":
	move(sys.argv[1], sys.argv[2], sys.argv[3])