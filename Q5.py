import time
import random

numbers = []

def generate_number():
  for i in range(1,1000001):
    a = random.randint(0,1000000)
    numbers.append(a)

def sorting():
    start_time = time.time()
    generate_number()       #1,000,000개 리스트 생성
  
    numbers.sort()
    end_time = time.time()

    elapsed = end_time - start_time

    print(numbers[:10])
    print(f"실행시간 : {elapsed:.2f}초")

    if elapsed and elapsed <3:
        print('PASSCORD = ','TRUE')
    else:
        print('PASSCORD = ','FALSE')

sorting()

'''
[2, 2, 3, 3, 3, 3, 5, 6, 6, 6]
실행시간 : 0.68초
PASSCORD =  TRUE
'''