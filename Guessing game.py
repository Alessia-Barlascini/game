secret_word = 'python'
your_guess = ''

#while loop to ask for a word until the input is right
while your_guess != secret_word:
    your_guess = input('Enter your guess: ')
print('you win!')