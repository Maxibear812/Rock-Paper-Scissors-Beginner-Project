import time

print("Welcome to my computer quiz!")

#User inputs their name to begin the game. 
playing = input("Do you want to play? ")
if playing.casefold() == "Yes".casefold():
    time.sleep(0.5)
    print("Okay! Let's play :) ")
elif playing.casefold() != "Yes".casefold():
    time.sleep(0.5)
    print("Okay, thanks for your time! Goodbye")
    time.sleep(1)
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.casefold() == "Central Processing Unit".casefold():
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")
    time.sleep(1) #Gives user a moment to read before moving on

answer = input("What does GPU stand for? ")
if answer.casefold() == "Graphics Processing Unit".casefold():
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")
    time.sleep(1) #Gives user a moment to read before moving on

answer = input("What does PSU stand for? ")
if answer.casefold() == "Power Supply Unit".casefold():
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")
    time.sleep(1) #Gives user a moment to read before moving on

answer = input("What does RAM stand for? ")
if answer.casefold() == "Random Access Memory".casefold():
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")
    time.sleep(1) #Gives user a moment to read before moving on

answer = input("What does SSD stand for? ")
if answer.casefold() == "Solid State Drive".casefold():
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")
    time.sleep(1) #Gives user a moment to read before moving on

score_percentage = (score / 5) * 100
print("You got " + str(score) + " questions correct! That's " + str(score_percentage) + " %")

time.sleep(1.0)
if score_percentage == 100: 
    print("You're a computer whiz! Why don't you do this for a living?")
elif score_percentage >=80:
    print("You're should be building your own computer at this point!. ")
elif score_percentage >=60:
    print("You did good, maybe work on memorizing those abbreviations!")
elif score_percentage >=40: 
    print("You should probably study more :/.")
elif score_percentage >=20:
    print("I'd recommend buying a prebuilt if you wanna game :/.")

time.sleep(1.5)
print("Thanks for playing!")
quit()