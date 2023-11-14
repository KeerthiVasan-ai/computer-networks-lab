def encrypt(string,shift):
    cipher = ""
    for char in string:
        if char == "":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char)+shift-65)%26+65)
        else:
            cipher = cipher + chr((ord(char)+shift-97)%26+97)
    return cipher

def decrypt(string,shift):
    plain = ""
    for char in string:
        if char == "":
            plain = plain + char
        elif char.isupper():
            plain = plain + chr((ord(char)-shift-65)%26+65)
        else:
            plain = plain + chr((ord(char)-shift-97)%26+97)
    return plain

text = input("Enter the String:")
shift = int(input("Enter the Shift number:"))

print("Plain Text",text)

cipher = encrypt(text,shift)

print("Encrypted Text",cipher)

plain = decrypt(cipher,shift)

print("Decrypted Text",plain)