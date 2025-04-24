import time
import random
import csv

numbers = []

def generate_number():        #숫자 무작위 생성
  for i in range(1,1000001):      #1,000,000번으로의 반복으로 1,000,000개 숫자 생성
    a = random.randint(1,1000000)       #random으로 1부터 1,000,000 사이의 숫자로 만들기
    numbers.append(a)       #무작위 숫자 list으로 생성

def sorting():
    start_time = time.time()   #시작 시간 
    generate_number()       #1,000,000개 리스트 생성

    numbers.sort()          #내장 함수 sort를 사용 -> numbers 리스트 내에서 정렬

    end_time = time.time()  #리스트 생성 및 정렬하기 까지 걸린 측정 종료

    elapsed = end_time - start_time     #시간 확인하기 (종료시간-시작시간)

    print(numbers[:10])     #정렬된 숫자 리스트 앞에 10개만 출력
    print(f"실행시간 : {elapsed:.2f}초")    #실행시간, 소숫점 둘째자리까지만 출력

    if elapsed and elapsed <3:        #잘 생성됐는지, 소요된 시간이 3초 이내 인지 확인 -> 맞으면 TRUE, 아니면 FALSE
        print('PASSCORD = ','TRUE')
        
        with open("output.csv", mode="w",newline='') as file:     #output.csv 파일을 생성해서 정렬된 숫자 리스트를 파일에 넣음
          writer = csv.writer(file)
          for item in numbers:
            writer.writerow([item])     #정렬된 숫자를 하나씩 나열하고 한 칸에 하나씩 숫자 삽입

    else:
        print('PASSCORD = ','FALSE')

sorting()     #함수 실행

#출력예시
'''   
[2, 3, 3, 5, 5, 5, 6, 7, 7, 7]
실행시간 : 0.69초
PASSCORD =  TRUE
'''