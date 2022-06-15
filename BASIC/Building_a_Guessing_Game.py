# MENGGUNAKAN WHILE LOOP contoh ke 1
# secret_word = "giraffe"
# guess = ""

# while guess != secret_word:
#     guess = input("Enter guess: ")

# print("You win!")

# CONTOH KE 2 COUNT DAN LIMIT
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
