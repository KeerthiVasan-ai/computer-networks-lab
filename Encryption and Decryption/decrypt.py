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