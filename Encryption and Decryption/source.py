import encrypt as ept
import decrypt as dpt

text = input("Enter the String:")
shift = int(input("Enter the Shift number:"))

print("Plain Text",text)

cipher = ept.encrypt(text,shift)

print("Encrypted Text",cipher)

plain = dpt.decrypt(cipher,shift)

print("Decrypted Text",plain)