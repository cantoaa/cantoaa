import random
password = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
passwordL = ""


def CreatePassword():
    print("How much letters or numbers you want on your password?")
    numberletters = int(input("Number of Letters: "))
    numbernumbers = int(input("Number of numbers: "))
    lettersnumbers = numberletters + numbernumbers
    for CreatingPassword in range(lettersnumbers):
        Mdecision = random.randint(0,1)
        print(Mdecision)
        print(numberletters)
        password.append("")
        if Mdecision == 0 and numberletters > 0:
            password[CreatingPassword] = alphabet[random.randint(0,25)]
            numberletters = numberletters - 1
        elif Mdecision == 1 and numbernumbers > 0:
            password[CreatingPassword] = numbers[random.randint(0,9)]
            numbernumbers = numbernumbers - 1
    print("Your Password: " + passwordL.join(password))

CreatePassword()