# -*- coding:utf-8 -*-
# File: ifdefextract.py
# Author: Arves100
# Date: 14-05-2020
# License: MIT
#
import os

INCLUDE_FILES = [ ".cpp", ".c", ".h", ".hpp" ]
EXCLUDE_DIRECTORIES = [ "bin", ".vs" ]
CONTENT_COPY_RANGE = 10

class IfdefExtract:
	def __init__(self):
		self.macroName = ""
		self.inputDir = ""
		self.outputDir = ""
		self.fileContent = []
		
	def getOutputDir(self):
		return self.outputDir
	
	def getInputDir(self):
		return self.inputDir
	
	def getMacroName(self):
		return self.macroName
		
	def setOutputDir(self, outputDir):
		self.outputDir = outputDir
	
	def setInputDir(self, inputDir):
		self.inputDir = inputDir
		
	def setMacroName(self, macroName):
		self.macroName = macroName

	def prompt(self):
		self.macroName = input("Please input the macro name: ")
		self.inputDir = input("Directory to search: ")
		self.outputDir = input("Output directory: ")
	
	def makeDir(self, directory):
		try:
			os.makedirs(directory)
		except:
			#print("Directory {} is already created!".format(directory))
			pass
			
	def listDirAndExecute(self):
		dirs = os.listdir(self.inputDir)
		
		for directory in dirs:
			if directory in EXCLUDE_DIRECTORIES or directory == self.outputDir:
				continue
			
			self.processDir(os.path.join(self.inputDir, directory))

	def processDir(self, directory):
		for root, dirs, files in os.walk(directory, topdown=True):
			for file in files:
				if self.isFileIncluded(file):
					self.processFile(file, root)
	
	def isFileIncluded(self, file):
		for extension in INCLUDE_FILES:
			if file.endswith(extension):
				return True

		return False
	
	def processFile(self, fileName, directory):
		self.fileContent = []
		completeFileName = os.path.join(directory, fileName)
		macroFound = 0
	
		try:
			file = open(completeFileName, "r", encoding="utf-8")
			fileContent = file.readlines()
			file.close()
		except UnicodeError:
			try:
				file = open(completeFileName, "r")
				fileContent = file.readlines()
				file.close()
			except UnicodeError:
				if file:
					file.close()

				print("ERROR: Invalid encoding of file {}".format(completeFileName))
				return				
			except:
				if file:
					file.close()
					
				print("ERROR: Error during process of {}".format(completeFileName))
				return				
		except:
			if file:
				file.close()
				
			print("ERROR: Error during process of {}".format(completeFileName))
			return			

		try:
			currentLine = 0
			
			ifdefCount = 0			
			for line in fileContent:
				if "#ifdef {}".format(self.macroName) in line:
					if currentLine > CONTENT_COPY_RANGE:
						self.fileContent.append("// Search:\n")
						for k in range(CONTENT_COPY_RANGE):
							self.fileContent.append(fileContent[currentLine-CONTENT_COPY_RANGE+k])
					
					self.fileContent.append("// Add:\n")
					self.fileContent.append(line)
					ifdefCount += 1
				elif "#ifdef" in line and ifdefCount > 0:
					self.fileContent.append(line)
					ifdefCount += 1
				elif "#endif" in line and ifdefCount > 1:
					self.fileContent.append(line)
					ifdefCount -= 1
				elif "#endif" in line and ifdefCount == 1:
					self.fileContent.append(line)
					self.fileContent.append("//--------------------------\n")
					self.fileContent.append("\n")
					ifdefCount -= 1
					macroFound += 1
				elif ifdefCount > 0:
					self.fileContent.append(line)
					
				currentLine += 1

			if ifdefCount > 0:
				print("WARNING: Missing #endif for file {}, result may be inaccurate!".format(completeFileName))
			
			if ifdefCount < 0:
				print("WARNING: Missing a #ifdef for file {}, result may be inaccurate!".format(completeFileName))
		except:
			print("ERROR: Error during process of {}".format(completeFileName))
			return
			
		if macroFound > 0:
			self.saveFile(fileName, directory, macroFound)
		
	def saveFile(self, fileName, directory, macroFound):
		completeFileName = os.path.join(directory.replace(self.inputDir, self.outputDir), fileName)

		print("INFO: Saving file {} with {} macro(s) found".format(completeFileName, macroFound))
		self.makeDir(os.path.join(self.outputDir, directory))
		
		try:
			os.remove(completeFileName)
		except:
			#print("ERROR: Cannot remove file {}, result may be inaccurate!".format(completeFileName))
			pass
		
		try:
			file = open(completeFileName, "w", encoding="utf-8")
			for line in self.fileContent:
				file.write(line)
			file.close()
		except:
			print("ERROR: Error while saving file {}".format(completeFileName))
			
if __name__ == "__main__":
	print("Ifdef extract v1.0 by Arves100")
	ifs = IfdefExtract()
	ifs.prompt()
	ifs.makeDir(ifs.getOutputDir())
	print("INFO: Processing...")
	ifs.listDirAndExecute()
	print("INFO: Done! Saved in {}".format(ifs.getOutputDir()))

# EOF
