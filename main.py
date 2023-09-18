alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
def encrypt(plainText,shiftAmount):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"encoded text is {cipherText}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
def decrypt (encodeText , shiftAmount):
    decodedText = ""
    for letter in encodeText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount
        newLetter = alphabet[newPosition]
        decodedText += newLetter
    print(f"decoded text is {decodedText}")
    
if direction == "encode":
    encrypt(plainText=text, shiftAmount= shift)
elif direction == "decode":
    decrypt(encodeText=text , shiftAmount=shift)
else:
    print("wrong text")