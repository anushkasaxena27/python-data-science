import random

while True:
    input('Enter to roll dice 🎲') #fake input to simulate user input
    roll = random.randint(1,6)
    print('You rolled dice and got: ',roll)
    if roll == 6:
        print('🏆YOU WIN🏆')
        break
    elif roll == 1:
        print('☠️ YOU LOSE!☠️')
        break
    else:
        print('Keep rolling...')