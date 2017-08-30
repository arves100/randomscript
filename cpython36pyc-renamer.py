import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Rename CPython-36 Pyc to Pyc files.')
parser.add_argument('path', metavar='Path', help='A path were to rename files')
args = parser.parse_args()
mypath = args.path

def Rename(path):
	if not os.path.exists(path):
		print("Error: cannot find folder " + path)
		return
	if not os.path.isdir(path):
		print("Error: " + path + " is not a directory")
		return
		
	for filename in os.listdir(path):
		if filename.endswith(".cpython-36.pyc"):
			os.rename(path + "/" + filename, path + "/" + filename[:len(filename) - 15] + ".pyc")
	
#def TestName(path):
#	filename = path
#	if not filename.endswith(".cpython-36.pyc"):
#		return # Bad
#	print(len(filename))
#	print(filename[:len(filename) - 15])
	
Rename(mypath)