import random

score = 0
alive = True
answer = ""
PGuess = ""

data = [
        {
        'name' : "Instagram",
        'follower_count' : 346,
        'description' : 'Social media platform',
        'country' : 'United States'
        },
        {
        'name' : "Jordan Barrett",
        'follower_count' : 4400000,
        'description' : 'Masculine Model',
        'country' : 'United States'
        },
        {
        'name' : "Neymar",
        'follower_count' : 229000000,
        'description' : 'Soccer Player',
        'country' : 'Brazil'
        },
        {
        'name' : "Cantoaa",
        'follower_count' : 44,
        'description' : 'Computer Engineer',
        'country' : 'Brazil'
        },
        {
        'name' : "UFSC Araranguá",
        'follower_count' : 7740,
        'description' : 'Santa Catarina University',
        'country' : 'Brazil'
        },
        {
        'name' : "MIT",
        'follower_count' : 853000,
        'description' : 'Massachussets Institute of Technology',
        'country' : 'United States'
        },
        {
        'name' : "Mr Beast",
        'follower_count' : 66900000,
        'description' : 'Content Creater',
        'country' : 'United States'
        },
        {
        'name' : "Elon Musk",
        'follower_count' : 2800000,
        'description' : 'Ceo of Tesla',
        'country' : 'South Africa/United States'
        },
        {
        'name' : "Bill Gates",
        'follower_count' : 11500000,
        'description' : 'Ceo of Microsoft',
        'country' : 'United States'
        }
]
print("Welcome to the HigherLower game!")
while alive:
    if len(data) > 1:
        candidateA = data[random.randint(0,len(data)- 1)]
        data.remove(candidateA)
        candidateB = data[random.randint(0,len(data) - 1)]
        data.remove(candidateB)
    else:
        print("Congratulations, you won the game!")
        print(f"Final Score: {score}")
        if input("Want to continue(y/n) \n") == "y":
                data = [
            {
            'name' : "Instagram",
            'follower_count' : 346,
            'description' : 'Social media platform',
            'country' : 'United States'
            },
            {
            'name' : "Jordan Barrett",
            'follower_count' : 4400000,
            'description' : 'Masculine Model',
            'country' : 'United States'
            },
            {
            'name' : "Neymar",
            'follower_count' : 229000000,
            'description' : 'Soccer Player',
            'country' : 'Brazil'
            },
            {
            'name' : "Cantoaa",
            'follower_count' : 44,
            'description' : 'Computer Engineer',
            'country' : 'Brazil'
            },
            {
            'name' : "UFSC Araranguá",
            'follower_count' : 7740,
            'description' : 'Santa Catarina University',
            'country' : 'Brazil'
            },
            {
            'name' : "MIT",
            'follower_count' : 853000,
            'description' : 'Massachussets Institute of Technology',
            'country' : 'United States'
            },
            {
            'name' : "Mr Beast",
            'follower_count' : 66900000,
            'description' : 'Content Creater',
            'country' : 'United States'
            },
            {
            'name' : "Elon Musk",
            'follower_count' : 2800000,
            'description' : 'Ceo of Tesla',
            'country' : 'South Africa/United States'
            },
            {
            'name' : "Bill Gates",
            'follower_count' : 11500000,
            'description' : 'Ceo of Microsoft',
            'country' : 'United States'
            }]
        else:
            break

    print(f"Compare {candidateA['name']}, {candidateA['description']}, from {candidateA['country']}, follower count ")
    print("To")
    print(f"{candidateB['name']}, {candidateB['description']}, from {candidateB['country']}, follower count")
    if candidateA['follower_count'] > candidateB['follower_count']:
        answer = candidateA['name']
    else:
        answer = candidateB['name']
    if input("Who has more followers? \n").lower() == answer.lower():
        score += 1
        print("You got the right answer!")
        print(f"Score: {score}")
    else:
        alive = False
        print("Wrong answer :(")
        print(f"Final Score: {score}")
