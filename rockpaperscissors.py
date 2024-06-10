import random
import time

def play():
    user = input("Lets play? 'r' for rock,'p' for paper, 's' scissors ")
    computer = random.choice(['r', 'p', 's'])
    time.sleep(0.5)
    print(f"Computer's choice: {computer}")
   
    if user == computer:
       return 'Its a tie'
    
    if is_win(user, computer):
       return'Yay! You won'
    
    return'Sorry! you lost'

def is_win(player, opponent):
        
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
           return True
      
print(play())