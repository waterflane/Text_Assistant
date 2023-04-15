from datetime import datetime
import time
import random

i = 0
never = input('Нажмите Enter что-бы начать...')
timer = []
time = []
Win = True

while i < 5:
    first_numb = random.randint(1, 100)
    second_numb = random.randint(1, 100)
    sign = random.randint(1, 2)
    if sign == 1:
        result = first_numb + second_numb
        print(f'{first_numb} + {second_numb} = ')
    else:
        result = first_numb - second_numb
        print(f'{first_numb} + {second_numb} = ')
    start = datetime.now()
    timer.append(int(input()))
    if result == timer[i]:
        Win = True
    elif result != timer[i]:
        Win = False
        i = 9
    finish = datetime.now()
    time.append(finish - start)
    print(f'Время: {finish - start}')
    i = i + 1
    
if Win == True:
    Time = time[0] + time[1] + time[2] + time[3] + time[4]
    Time = Time / 5
    print(f'Ваш средний результат: {Time}')
if Win == False:
    print('Вы проиграли!')
    
