# while loop
# word guess game
"""
SECRET_WORD = "WORD"

user_guess_word = ""
guess_number = 0
guess_number_limit = 3
is_out_of_guess_limit = False

user_name = input("Your name: ")

while user_guess_word != SECRET_WORD and not(is_out_of_guess_limit):
    if(guess_number < guess_number_limit):
        user_guess_word = input("Enter you guess word: ").upper()
        guess_number += 1
    else:
        is_out_of_guess_limit = True

if is_out_of_guess_limit:
    print(user_name + " LOSS")
else:
    print(user_name+" wins")

"""

# for loop

for i in range(10):
    print(i)
