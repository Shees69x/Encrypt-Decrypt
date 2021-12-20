def encrypt(text,shift):
    output = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            output += chr((ord(char) + shift-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            output += chr((ord(char) + shift - 97) % 26 + 97)
 
    return output
 
#check the above function
text = str(input("Enter the plain text message that you want to encrypt : "))
shift = int(input("Enter the number of shift: "))

print ("\nOriginal String  : " + text)
print ("Shift : " + str(shift))
print ("Encrypted String : " + encrypt(text,shift))


def decrypt(ciphertext,shift):

	output = ""

	# traverse text

	for i in range(len(ciphertext)):

		char = ciphertext[i]

		# Encrypt uppercase characters

		if (char.isupper()):

			output += chr((ord(char) - shift-65) % 26 + 65)

		# Encrypt lowercase characters

		else:
			output += chr((ord(char) - shift - 97) % 26 + 97)

	return output





ciphertext = str(input("Enter the plain text message that you want to decrypt : "))
shift = int(input("Enter the number of shift: "))

print ("\nEncrypted String : " + ciphertext)
print ("Shift : " + str(shift))
print ("Original String: " + decrypt(ciphertext,shift))