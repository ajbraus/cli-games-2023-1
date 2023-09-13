
# THIS FUNCTION IS A DICE GAME THAT SHOULD
# * ROLE ONE SIX SIDED DICE
# * ASK YOU TO PLAY AGAIN

# import random

# inp = input('roll the dice? y/n: ')
# print(inp)

# if inp == "n":
#     print("OK. Come back soon!")
# elif inp == "y":
#     # num = random.random()
#     six_sided_die = [1, 2, 3, 4, 5, 6]
#     num = random.choice(six_sided_die)
#     print(num)
# else:
#     print("beep-boop, I did not understand that input. Please try again")


import random

def roll_die():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    
    while True:
        input("Press Enter to roll the die...")
        
        roll_result = roll_die()
        print(f"You rolled a {roll_result}!")
        
        play_again = input("Do you want to roll again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
