# 화성 수학

# @는 3을 곱하고 %는 5를 더하고 #은 7을 빼는 연산자 

T = int(input())

for i in range(T):
    case = list(map(str, input().split()))
    res = float(case[0])
    
    for y in range(len(case)):
        if case[y] == '@':
            res *= 3
        elif case[y] == '%':
            res += 5
        elif case[y] == '#':
            res -= 7
        
    print("%.2f" %res)