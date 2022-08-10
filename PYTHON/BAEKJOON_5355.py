# 화성 수학

# @는 3을 곱하고 %는 5를 더하고 #은 7을 빼는 연산자 

T = int(input())

for i in range(T):
    case = list(map(str, input().split())) #case에 문열을 입력 받아 분할
    res = float(case[0]) # 리스트의 첫  번째 문자열을 res에 저장
    
    for y in range(len(case)): # case 길이만큼 반복 (연산자의 수만큼 연산자 계산) 
        if case[y] == '@':  
            res *= 3
        elif case[y] == '%':
            res += 5
        elif case[y] == '#':
            res -= 7
        
    print("%.2f" %res)
