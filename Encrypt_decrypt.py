letters='abcdefghijklmnopqrstuvwxyz'
def encrypt(text,key):
    ciphertext=" "
    for letter in text:
        letter=letter.lower()
        if not letter==" ":
            index=letters.find(letter)
            if index==-1:
                ciphertext=ciphertext+letter
            else:
                new_index=index+key
                if new_index>=26:
                    new_index=new_index-26
                ciphertext=ciphertext+letters[new_index]
    return ciphertext

def decrypt(ciphertext,key):
    text=" "
    for letter in ciphertext:
        letter=letter.lower()
        if not letter==" ":
            index=letters.find(letter)
            if index==-1:
                text=text+letter
            else:
                new_index=index-key
                if new_index<0:
                    new_index=new_index+26
                text=text+letters[new_index]
    return text




print()
print("Caesar-cipher program")
print()
print("do you want to encrypt or decrypt")
userinput=input("Enter e/d:").lower()
print()
if(userinput=="e"):
    print("Encyption selected")
    key=int(input("Enter key:"))
    text=input("The text to be encypted is:")
    ciphertext=encrypt(text,key)
    print("Ciphertext is:"+ciphertext)
elif(userinput=="d"):
    print("Decryption selected")
    key=int(input("Enter key:"))
    text=input("The text to be decrypted is:")
    plaintext=decrypt(text,key)
    print("Plaintext is:"+plaintext)
