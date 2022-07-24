'''Игра: Угадай число. 
ПК загадывает число, затем отгадывает его. 
После отгадывает число менее чем за 20 попыток.
'''

# from itertools import count
import numpy as np

def random_predict(number:int=1) -> int: 
    """
    Function for random guess the number. 
    Number is defaults to 1.

    Returns:
        int: number of guesses.
    """
    count = 0
    
    while True: 
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number: 
            break
    return count

print(f'Number of attempts is {random_predict()}.')

def score_game(random_predict) -> int: 
    """For how many attempts on average out of 1000 approaches does our algorithm guess.
        За сколько в попыток ПК отгадает число в среднем.

    Args:
        random_predict (_type_): guess the number

    Returns:
        int: integer, average number of attempts
    """
    count_list = [] # list for save the number of attempts
    # np.random.seed(1) # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers
    
    for number in random_array: 
        count_list.append(random_predict(number))
    
    score = int(np.mean(count_list)) # find the average number of attempts
    
    print(f'Your algorithm guesses the number in an average of {score} attempt(s).')
    return score

def random_predict_less_20(number) -> int: 
    """ПК угадывает случайное число от 1 до 101, затрачивая не более 20 попыток.
    
     Args:
        number (int, optional): Загаданное число.
        
    Returns:
        int: Число попыток
    """
    count = 0
    min = 1 
    max = 101
    
    while True: 
        count += 1 
        mid = round((min + max) / 2)
        
        if mid > number: 
            max = mid
        elif mid < number: 
            min = mid
        else: 
            break
        
    return(count)
    print(f'Количество попыток: {random_predict_less_20(number)}')

# Run
if __name__ == '__main__': # the condition to run when the file is executable
    score_game(random_predict) # not called when the file is being imported