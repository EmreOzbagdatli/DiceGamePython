import random
print("Welcome to Dice roll program.")
roll_again = "yes"
min = 1
max = 6
while roll_again == "yes":
    print("Dice is rolling...")
    dice1 = random.randint(min,max)
    dice2 = random.randint(min,max)
    print("First dice is : ",dice1)
    print("Second dice is : ",dice2)

    roll_again = input("Roll the dices again? (yes),(no) :")
    if roll_again == "no":
        print("The End!")
        break
    if roll_again != "yes" or "no":
        print("Wrong answer.")



