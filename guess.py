import random
#STORE_TOP_SCORERS = 200
old_high_score = 0
old_high_scorer = ""
second_old_high_score = 0
second_old_high_scorer = ""
try:
    f = open("score.txt", "r")
    score = f.read()
    score_data = score.split(",")
    old_high_scorer = score_data[0]
    old_high_score = int(score_data[1])
    print("HIGH SCORE")
    print(f"{old_high_scorer} - {old_high_score}")
except:
    print("You are the first player")


try:
    f = open("2nd score.txt", "r")
    score = f.read()
    second_score_data = score.split(",")
    second_old_high_scorer = second_score_data[0]
    second_old_high_score = int(score_data[1])
    print("2ND HIGH SCORE")
    print(f"{second_old_high_scorer} - {second_old_high_score}")
except:
    print("You are the second player")


print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")
secret_number = random.randint(1, 100)
print("I have decided the number. Now its your choice to guess the number I decided. Keep in mind you only have 10 attempts")
attempt = 0
found = False
print(secret_number)
while attempt < 10:
    answer = int(input("Enter number:"))
    attempt = attempt + 1
    if answer == secret_number:
        found = True
        break 
    elif answer >= secret_number:
        print("Number is higher.")
    elif answer <= secret_number:
        print("Number is lower")
if found == True:
    print("Correct answer")
    print(f"You gussed answer in {attempt}")
if attempt <= old_high_score:
    name = input("What is your name ")
    f = open("score.txt", "w")
    f.write(f"{name},{attempt}")
    f.close()
if attempt >= second_old_high_score:
    name = input("What is your name ")
    f = open("2nd score.txt", "w")
    f.write(f"{name},{attempt}")
    f.close()

else:
    print("Attempts over")
