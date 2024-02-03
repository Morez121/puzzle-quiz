print("Welcome to my game!")

answer = input("do you want to play?")
if answer  != "yes":
    quit()

user_points = 0

Question_1 = input("What is the capital of Switzerland?").lower().strip()
if Question_1 == 'has no capital' or Question_1 =='no capital':
    print("Correct. + 3 points") 
    # user_points = user_points + 3
    user_points += 3
else: 
    print(" Wrong answer! -1 point")
    # user_points = user_points - 1
    user_points -= 1

Question_2 = input("What is the fastest animal on the planet?")
if Question_2.lower().strip() == 'cheeta':
    print("You got this! + 3 points")
    user_points = user_points + 3

else:
    print("Wrong answer! -1 point")
    user_points = user_points - 1

print(f" your total point is = {user_points}" )