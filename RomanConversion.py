print("Welcome to a Roman Number Conversor")
print("It can only convert below 5000")
RomanN = {
        'I': 1,
        'V' : 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M' : 1000
        }
RomanNInverse = {
        1: 'I',
        5 : 'V',
        10 : 'X',
        50 : 'L',
        100: 'C',
        500 : 'D',
        1000 : 'M'
        }

typeNumber = input("Roman to Integer or Integer to Romar?(RI)(IR) ")
sumOfNums = 0
sumOfLetters = []
number = input("What number you wanna convert: ")
currentvalue = 0
position = 0
currentletter = ""
if typeNumber == "RI":
    for RTI in reversed(number):
        if currentvalue > RomanN[RTI]:
            sumOfNums -= RomanN[RTI]
            currentvalue = RomanN[RTI]
        else:
            currentvalue = RomanN[RTI]
            sumOfNums += currentvalue
    print(sumOfNums)
else:
    number = str(number)
    for ITR in reversed(number):
        ITR = int(ITR)
        while ITR > 0:
            number = str(number)
            if ITR == 0:
                break
            elif (ITR < 9 and ITR != 5) or ITR < 4: 
                sumOfLetters.append(RomanNInverse[10 ** position])
                number = int(number)
                number -= 10 ** position
                ITR -= 1
            elif ITR == 4 or ITR == 9:
                number1 = 0
                number2 = 0
                if ITR == 4:
                    number1 = RomanNInverse[((ITR + 1) * 10 ** position) - 4 * 10 ** (len(number) - 1)]
                    sumOfLetters.append(number1)
                else:
                    number1 = RomanNInverse[((ITR + 1) * 10 ** position) - 9 * 10 ** (len(number) - 1)]
                    sumOfLetters.append(number1)
                number2 = RomanNInverse[(ITR + 1) * 10 ** (len(number) - 1)]
                sumOfLetters.append(number2)
                number = int(number)
                number -= (RomanN[number2] - RomanN[number1])
                ITR -= ITR
            elif ITR == 5:
                sumOfLetters.append(RomanNInverse[ITR * 10 ** position])
                number = int(number)
                number -= ITR * 10 ** (position)
                ITR -= ITR
        position += 1
    sumOfLetters.reverse()
    print(sumOfLetters)

            
