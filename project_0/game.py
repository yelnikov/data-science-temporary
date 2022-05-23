'''Game: Find a number'''

import numpy as np

number = np.random.randint(1,101)
count = 0 

while True:
    count += 1
    predict_number = int(input('Guess the number of 1 to 100! Enter: '))
    
    if predict_number > number: 
        print('The number must be smaller!')
    elif predict_number < number: 
        print('The number must be higher!')
    else: 
        print(f'You have found an ansver in {count} attempts, the number is {number}!')
        break
    
    