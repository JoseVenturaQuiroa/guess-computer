import random

while True:
    try:
        smaller = int(input("Enter the smaller number: "))
        break
    except:
        print("Please enter an integer.")

while True:
    try:
        larger = int(input("Enter the larger number: "))
        break
    except:
        print("Please enter an integer.")

while True:
    try:
        userNumber = int(input("Enter your guess: "))
        break
    except:
        print("Please enter an integer.")

count = 0
userNumberStr = str(userNumber)
while True:
    count += 1
    compNumber = random.randint(smaller, larger)
    if userNumber > compNumber:
        print(str(compNumber) + ": Too small")
    elif userNumber < compNumber:
        print(str(compNumber) + ": Too large")

    else:
        countStr = str(count)
        print("I got " + userNumberStr + " in " + countStr + " tries!")
        break
