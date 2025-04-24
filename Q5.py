import time
import random

numbers = []

def generate_number():
  for i in range(1,1000001):
    a = random.randint(0,1000000)
    numbers.append(a)

def sorting():
  generate_number()       #1,000,000개 리스트 생성

  start_time = time.time()
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
[0, 2, 2, 3, 4, 7, 9, 9, 9, 10]
실행시간 : 0.15초
PASSCORD =  TRUE
'''