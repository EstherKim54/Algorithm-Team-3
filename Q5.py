import time
import random
import csv

numbers = []

def generate_number():        #숫자 무작위 생성
  for i in range(1,1000001):      #1,000,000번으로의 반복으로 1,000,000개 숫자 생성
    a = random.randint(1,1000000)       #random으로 1부터 1,000,000 사이의 숫자로 만들기
    numbers.append(a)       #무작위 숫자 list으로 생성

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
        
        with open("output.csv", mode="w",newline='') as file:
          writer = csv.writer(file)
          for item in numbers:
            writer.writerow([item])

    else:
        print('PASSCORD = ','FALSE')

sorting()

'''
[2, 3, 3, 5, 5, 5, 6, 7, 7, 7]
실행시간 : 0.69초
PASSCORD =  TRUE
'''