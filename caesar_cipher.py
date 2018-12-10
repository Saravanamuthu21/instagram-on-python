def encrypt(text, s):
    result = ""


# transverse the plain text
    for i in range(len(text)):
        char = text[i]
    # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
    # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
# check the above function
def decrypt(text, s):
    result1 = ""


# transverse the cipher text
    for j in range(len(text)):
        char = text[j]
    # Decrypt uppercase characters in cipher text

        if (char.isupper()):
            result1 += chr((ord(char) - s - 65) % 26 + 65)
    #Decrypt lowercase characters in cipher text
        else:
            result1 += chr((ord(char) - s - 97) % 26 + 97)
    return result1
text = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))

print("Cipher: " + encrypt(text, s))
v = encrypt(text, s)
print(decrypt(v,s))
