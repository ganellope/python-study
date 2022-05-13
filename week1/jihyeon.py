# 지현 1. [1, 2, 3, 4, 5, 6, 7, 8]이라는 값이 들어있는 test_list가 있다. 결과값이 [3, 4, 5, 6]으로 나오게 슬라이싱하는 방법 3가지를 작성하시오
"""
test_list[2: 6]
test_list[-6: -2]
test_list[2: -2]
"""

# 지현 2. [1, 2, 3, 4, 5, 6, 7, 8]이라는 값이 들어있는 test_list를 출력하는 반복문을 시퀀스와 range()함수를 이용하여 2가지 방법으로 작성하시오
"""
for num in test_list: print(num)
for i in range(8): print(test_list[i])
"""

# 지현 3. 영문자를 입력받아, 해당 영문자를 소문자, 대문자, 역순으로 출력 (입력받은 값이 영문자인지 따로 체크는 X)
"""
eng = input()
print(eng.upper())
print(eng.lower())
print(eng[::-1])
"""

# 지현 4. def thisisfunc(param1, param2 = ‘a’, param3 = ‘b’) 이라는 함수를 호출할 수 있는 방법을 3가지 이상 작성하시오
"""
thisisfunc(’p’)
thisisfunc(’p’, ‘c’)
thisisfunc(’p’, ‘c’, ‘d’)
thisisfunc(’p’, param2 = ‘c’)
thisisfunc(’p’, param3 = ‘d’)
thisisfunc(’p’, param3 = ‘d’, param2 = ‘c’)
thisisfunc(param3 = ‘d’, param2 = ‘c’, ‘p’)
"""

# 지현 5. [1, 2, 3, 4, 5, 6, 7, 8]이라는 값이 들어있는 test_list의 제곱값을 list로 return하는 함수를 람다와 map을 이용하여 작성하시오
"""
list(map(lambda x: x*x, test_list))
"""

# 가현 1. 두개의 정수를 입력받아 input함수와 print함수를 같이 사용하여 한 줄 프로그램을 완성
"""
a, b = map(int, input('정수 두 개를 입력하세요: ').split())
print(a, b)
"""

# 가현 2. 랜덤 함수를 이용해서 (1~10) 까지 맞출 때까지 while을 이용해 프로그램
"""
import random
randNum = random.randint(1, 10)
while True:
    guessNum = int(input("숫자를 입력하세요: "))
    if(guessNum == randNum):
        print("정답")
        break
"""

# 가현 3. 한개의 enum을 생성해 사용자가 입력받은 값을 통해 match case 문을 이용해 출력 (기타 제어 흐름 도구)
"""
from enum import Enum
class Rainbow(Enum):
    빨 = 'RED'
    주 = 'ORANGE'
    노 = 'YELLOW'
    초 = 'GREEN'
    파 = 'BLUE'
    보 = 'PURPLE'
    분 = 'PINK'

color = input("빨주노초파보분 중에 하나를 입력하세요: ")

match color:
    case '빨':
        print(Rainbow.빨.value)
    case '주':
        print(Rainbow.주.value)
    case '노':
        print(Rainbow.노.value)
    case '초':
        print(Rainbow.초.value)
    case '파':
        print(Rainbow.파.value)
    case '보':
        print(Rainbow.보.value)
    case '분':
        print(Rainbow.분.value)
"""

# 가현 4. 람다 표현식을 이용해 영문자 5개 내림차순 정렬
"""
alph = ['a', 'v', 'c', 's', 'k']
print(sorted(alph, key=lambda x : x[0], reverse = True))
"""

# 가현 5. 함수의 기본값(인자 기본값)이 계속되는 호출 시 누적되지 않도록 list에 append하는 함수 생성
"""
"""

# 주혜 1. 한 개의 정수를 입력받은 뒤, 약수 리스트를 구하고, 구해진 약수의 각 거듭제곱 값을 모두 합한 값을 리턴하는 프로그램
"""
def func1():
    num = int(input("정수를 입력하세요: "))
    sum = 0
    print("약수: ", end="")
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")
            sum += (i*i)
    print("\n약수의 거듭제곱 합: ", end="")
    print(sum)
"""

# 주혜 2.
# 2개 이상의 단어로 이루어진 문자열을 입력받는다.(단어 간 스페이스바로 공백 넣기)
# - 각 단어의 알파벳의 위치가 홀수인 경우 => 대문자
# - 각 단어의 알파벳의 위치가 짝수인 경우 => 소문자
# 위 조건에 맞게 변경한 값을 리턴하는 프로그램
"""
def func2():
    words = [word for word in input().split()]
    for i in range(0, len(words)):
        if(i % 2 == 0):
            print(words[i].upper())
        else:
            print(words[i].lower())
"""

# 주혜 3. 연수 입력받아서 입력받은 수 만큼 별을 찍어봅시다! (가능하다면 리스트 컴프리헨션을 사용해봅시다)
"""
num = int(input("입력값: "))
for i in range(num+1):
    for j in range(num-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("")
"""

# 주혜 4.
# classOne = {'정지나':'여', '이대형':'남', '정혜선':'여', '제이슨':'남', '손주혜':'여'}
# classTwo = {'이가현':'여', '함기훈':'남', '박향규':'남', '이지현':'여', '신혜정':'여', '권오재':'남'}
# 1반과 2반의 학생들을 합친 뒤, 성별로 구분지어서 출력한다.
"""
def func3():
    classOne = {'정지나':'여', '이대형':'남', '정혜선':'여', '제이슨':'남', '손주혜':'여'}
    classTwo = {'이가현':'여', '함기훈':'남', '박향규':'남', '이지현':'여', '신혜정':'여', '권오재':'남'}
    allClass = dict(classOne, **classTwo)
    print("~ 여자 ~")
    for key, value in allClass.items():
        if '여' == value:
            print(key)
    print("\n~ 남자 ~")
    for key, value in allClass.items():
        if '남' == value:
            print(key)
"""

# 주혜 5. 정수 10개를 입력받고, 10개의 숫자 중 가장 작은 값, 가장 큰 값, 중간 값을 출력한다.
"""
print("정수 10개를 입력하세요(공백으로 구분)")
nums = [int(i) for i in input().split()]
nums.sort()
print("가장 큰 값: " + str(max(nums)))
print("중간 값: " + str(nums[int(10/2)]))
print("가장 작은 값: " + str(min(nums)))
"""