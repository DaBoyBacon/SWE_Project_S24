import sys

def getAPIKey():
	filename = sys.path[0]+"\\..\\..\\..\\..\\apiKey.txt"
	file = open(filename, "r")
	line = file.read()
	#print(line)
	return line
	
getAPIKey()