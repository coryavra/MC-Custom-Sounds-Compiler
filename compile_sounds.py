#!/usr/bin/python
import os, sys, json

def main():

	# Set the current working directory
	os.chdir(os.path.dirname(sys.argv[0]))

	# Update the file structure with any new directories
	updateTree()

	# Retrieve all sound events and compile them into a JSON file
	updateSounds()

class soundEvent(object):

	def __init__(self, key, category):

		# Parse key into a filepath
		self.filePath = key.replace('.', '/')

		# Get the category from the event name
		self.category = category

		# Get all .ogg files at end of path
		self.soundFiles = []
		for file in os.listdir("../sounds/" + self.filePath):
			if file.endswith(".ogg"):

				# Add the path, remove the extension
				file = self.filePath + '/' + os.path.splitext(file)[0]

				# Music variant
				if self.category == "music" or self.category == "record":
					soundEventData = {
						"name":file,
						"stream":"true",
						"volume":0.2,
						"weight":1.0
					}
					self.soundFiles.append(soundEventData)

				# Step variant
				elif "step" in file:
					soundEventData = {
						"name":file,
						"volume":2.5,
					}
					self.soundFiles.append(soundEventData)

				# Default
				else:
					self.soundFiles.append(file)

def updateTree():

	# Read in the game's default sounds.json file
	with open("default_sounds.json") as data_file:
		defaultData = json.load(data_file)

	# Collect the top-level keys
	keylist = defaultData.keys()
	keylist.sort()

	# Get an list of all pre-existing directories
	originalDirectories = []
	for path, subdirs, files in os.walk("../sounds/"):

		# Log all empty directories
		if (os.listdir(path) == [] and path not in originalDirectories):
			originalDirectories.append(path)

		# Log all original directories
		for file in files:
			if path not in originalDirectories:
				if (file.endswith(".ogg")):
					originalDirectories.append(path)
			else:
				break

	# Create the file structure
	for key in keylist:

		# Parse key into a filepath
		keyFilePath = key.replace('.', '/') 
		keyFilePath = "../sounds/" + keyFilePath

		# Create the directory if it doesn't exist
		if not os.path.exists(keyFilePath):
			os.makedirs(keyFilePath)

		# Keep a log of all 
		else:
			if keyFilePath in originalDirectories:
				originalDirectories.remove(keyFilePath)
			else:
				print("Error: Misnamed file: " + keyFilePath)

	print("Empty Directories: ")
	for path, subdirs, files in os.walk("../sounds/"):

		# Make sure all filenames are lower-case for 1.11
		for file in files:
			os.rename(os.path.join(path, file), os.path.join(path, file.lower()))

		# Print all empty directories
		if (os.listdir(path) == []):
			print(path)

	print("Unused Directories: ")
	for file in originalDirectories:
		print(file)

def updateSounds():

	# Remove the old souds.json file, as we are about to write a new one
	try:
		os.remove("../sounds.json")
		print("Removed outdated sounds.json")
	except OSError:
		print("Cannot remove outdated sounds.json: No such file")
		pass

	# Read in the game's default sounds.json file
	with open("default_sounds.json") as data_file:    
		defaultData = json.load(data_file)

	# Collect the top-level keys
	keylist = defaultData.keys()
	keylist.sort()

	# Create an event for each key and append it to the file with all its sounds
	eventDictionary = {}
	for key in keylist:

		# Get the category depending on the version
		try:
			category = defaultData[key]["category"]
		except KeyError:
			category = key.split('.')[0]
			pass

		event = soundEvent(key, category) 	
		eventDictionary.update({
			key:({
				#"category":event.category, 
				"replace":"true", 
				"sounds":(event.soundFiles)
			})
		})

	# Finally, create a new sounds.json file to store the sound event dictionary 
	with open("../sounds.json", 'a') as outfile:
		json.dump(eventDictionary, outfile, sort_keys = True, indent = 2, ensure_ascii = False)
		print("Wrote new sounds.json!")

if __name__ == "__main__":
	main()