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