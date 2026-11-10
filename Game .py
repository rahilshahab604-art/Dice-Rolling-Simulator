import random

print("================================")
print("      DICE ROLLING GAME")
print("================================")

roll_count = 0
highest_score = 0

while True:

    choice = input("\nDo you want to roll the dice? (yes/no): ")

    if choice.lower() == "yes":

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total = dice1 + dice2

        roll_count += 1

        print("\nRolling the dice...")

        print("Dice 1:", dice1)
        print("Dice 2:", dice2)

        print("Total Score:", total)

        if total > highest_score:
            highest_score = total

        if dice1 == dice2:
            print("Congratulations! You got a DOUBLE!")

        if total == 12:
            print("WOW! You got the highest possible score!")

        print("\nTotal Rolls:", roll_count)
        print("Highest Score:", highest_score)

    elif choice.lower() == "no":

        print("\n================================")
        print("         GAME OVER")
        print("================================")

        print("Total Rolls:", roll_count)
        print("Your Highest Score:", highest_score)

        print("Thanks for playing!")

        break

    else:
        print("Invalid input! Please enter yes or no.")