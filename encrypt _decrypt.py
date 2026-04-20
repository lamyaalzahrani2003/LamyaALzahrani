import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "

chars = list(chars)

key = chars.copy()
random.shuffle(key)

#Encrypt
print(" -------Encryption-------")
plain_text = input("Enter Your Message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Encrypted Message is : {cipher_text}")    

#Decrypt
print(" -------Decryption-------")
cipher_text = input("Enter Your Message to Decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Decrypted Message is : {plain_text}")    