import random 

def guess(x):
    randomnum = random.randint(1, x)
    guess = 0
    while guess != randomnum:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess < randomnum:
            print('Sorry guess again.Too low,')
        elif guess > randomnum:
            print('Sorry, guess again.Too high')
    
    print(f'Yayy,you guess the number {randomnum} correctly.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high, if so type (H) or too low, if so type (L) :')
        if feedback == 'h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1 
    print(f"Yay! I guessed your number {guess}, correctly")    




    
computer_guess (100)