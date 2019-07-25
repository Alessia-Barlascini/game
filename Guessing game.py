secret_word = 'python'
your_guess = ''
guess_count = 0
guess_limit = 5

#while loop to ask for a word until the input is right
while your_guess != secret_word and guess_count < guess_limit:
    your_guess = input('Enter your guess: ')
    guess_count += 1                            #count the number of inputs

# different output depending on the right or false input
if your_guess == secret_word:
    print('you win!')
else:
    print('out of guesses, you lose!')