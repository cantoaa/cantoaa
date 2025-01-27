alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shift = 0
text = ""
textED = ""
start = 0

def Encode():
    text = input("What will be the text you want to encode? ")
    shift = int(input("What will be the shift of the words? "))
    textR = "Encoded Text: "

    for encrypt in range(len(text)):   
        if text[encrypt] in alphabet:
            positionA = alphabet.index(text[encrypt])
            textED = "".join(alphabet[(positionA + shift) % 26])
            textR += textED
        else:
            textR += text[encrypt]

    print(textR)
    if input("Do you want to continue? ").lower() == "yes":
        Decision()
        
    

def Decode():
    text = input("What will be the text you want to decode? ")
    shift = int(input("What was the shift of the encoded message? "))
    textR = "Decoded Text: "

    for decrypt in range(len(text)):
        if text[decrypt] in alphabet:
            positionA = alphabet.index(text[decrypt])
            textED = "".join(alphabet[(positionA - shift) % 26])
            textR += textED
        else:
            textR += text[decrypt]
    print(textR)
    if input("Do you want to continue? ").lower() == "yes":
        Decision()

def Decision():
    decision = input("Do you want to encode or decode? ").lower()
    if decision == "encode":
        Encode()
    else:
        Decode()

print("Welcome to the Caesar Cipher encoder and decoder.")
Decision()