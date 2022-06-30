a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b) 
print(a//b)
print(a%b)

""" 10869번 문제에서 주의할 점은 5번째 줄 a//b 이다

일반적으로 나누기를 할때 a/b 를 하면되지만 이렇게하면 소수점까지의 숫자가 나오기때문에
a//b 를 작성함으로써 몫만 출력되게 한다.
    """

