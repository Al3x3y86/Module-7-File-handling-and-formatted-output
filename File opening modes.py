from pprint import pprint

filt_name ='textFile.txt'
file = open("textFile.txt", mode="r")
file_content =file.read()
file.close()
pprint(file_content)
