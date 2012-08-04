# copy_files_by_date.py
# author: deebugger (deebug.dev@gmail.com)
#
# copy all image files of the form "yyyy-mm-dd..." to their corresponding
# directories (those being tgtDir/yyyy/mm/dd)
# useful for cleaning the Dropbox camera upload directory
#
# notice: this script doesn't delete any file, it just creates copies
#
# initial setup:
# - srcDir - where all the files are
# - tgtDir - parent directory for creating the yyyy/mm/dd directories

import sys, os, shutil

# fill these two!
srcDir = ""
tgtDir = ""

if srcDir == "" or tgtDir == "":
	print "--\n-- Fill in the srcDir and tgtDir correctly, then run again\n--"
	sys.exit

if not os.path.exists(tgtDir):
	os.makedirs(tgtDir)

allFiles = os.listdir(srcDir)

for file in allFiles:
	split = file[:10].split("-")
	if len(split) == 3:
		# construct the target directory
		year = split[0]
		month = split[1]
		day = split[2]
		targetDir = os.path.join(tgtDir, year, month, day)

		# make sure the file doesn't already exist in the target,
		# or print an error and move on (don't copy)
		targetPath = os.path.join(targetDir, file)
		if os.path.exists(targetPath):
			print "File: ", targetPath, " exists, skipping"
			continue

		# create the target directory, if it doesn't exist
		if not os.path.exists(targetDir):
			os.makedirs(targetDir)
		
		# copy the file
		shutil.copy2(os.path.join(srcDir, file), targetPath)
