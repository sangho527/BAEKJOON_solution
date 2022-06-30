a,b = map(int, input().split())
print(a+b)

 
"""
    1000번 파이썬 문제풀이
    
input은 숫자를 입력받는 것이지만 주의 할 점으로는 input 함수로 입력을 받으면 '문자열'로 입력을 받음 
split 함수는 입력받는 문자를 나눌 때 사용하는 함수 
이렇게 했을때 A, B = input().split()
A = int(A)
B = int(B)
print(x+y) 로도 가능하지만 깔끔하게 map 함수를 사용해서 표현가능
map(적용할 함수, 반복 가능한 자료형)이 기본형임 map을 사용해서 입력할때는 공백을 써주기
"""
