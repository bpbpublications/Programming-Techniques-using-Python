my_number = int(input("Guess the number between 1 and 100 : "))
my_match_num = 58
my_game_over = False
my_count = 0
while not my_game_over:
    if my_number == my_match_num:
        print(f"You guessed the number correctly in {my_count} times")
        my_game_over = True
    elif my_number < my_match_num:
        print("You guessed the number too low")
        my_count += 1
        my_number = int(input("Enter the number again: "))
    else:
        print("You guessed the number too high")
        my_count += 1
        my_number = int(input("Enter the number again: "))