a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0: #윤년의 코드
    print(1) #윤년이면
else:
    print(0) #윤년이 아니면