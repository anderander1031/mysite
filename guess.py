print('guess number')

import random
def guess():
    x = random.randint(0, 100)
    while True:
        try:
            a = int(input())
            print('a:', a)
            if a > x:
                print('too large')
            elif a < x:
                print('too small')
            else:
                print('hooray!!')
                break
        except:
            print('wrong input, please input again')


guess() 