import random
my_number = int(input("Guess the number between 1 amd 100 : "))
my_match_num = random.randint(1,100)
my_game_over = False
my_count = 0
while not my_game_over:
    if my_number == my_match_num:
        print(f"You guessed the number correctly in {my_count} times")
        my_game_over = True
    else:
        if my_number < my_match_num:
            print("You guessed the number too low")
        else:
            print("You guessed the number too high")
        my_count += 1
        my_number = int(input("Enter the number again: "))