import num as np

Message = "atheer"
K = 3
encryptedMessage = []
decryptedMessage = []

def encrypt(Message, shiftNum, encryptedMessage):
    for a in Message:
        # ord return the letter into ascii number
        letterInt = ord(a) - 97
        letter = (letterInt + shiftNum) % 26
        enryptedLetter = chr(letter+97)
        encryptedMessage.append(enryptedLetter)


def decrypt(encryptedMessage, shiftNum,decryptedMessage):
    for a in encryptedMessage:
        letterInt = ord(a) - 97
        letter = (letterInt - shiftNum) % 26
        enryptedLetter = chr(letter+97)
        decryptedMessage.append(enryptedLetter)

print(Message + " before encyrption")
encrypt(Message, K, encryptedMessage)
print("".join(encryptedMessage) + " after encryption")

print("".join(encryptedMessage) + " before decryption")
decrypt(encryptedMessage, K, decryptedMessage)
print ("".join(decryptedMessage) + " after decryption")




'''
def encrypt(letterInt, shiftNum):
    Y = (letterInt + shiftNum) % 26
    enryptedLetter = chr(Y+97)
    return enryptedLetter


for a in Message:

    # ord return the letter into ascii number
    letterInt = ord(a) - 97
    letter = encrypt(letterInt, K)
    encryptedMessage.append(letter)

print("".join(encryptedMessage))
'''
