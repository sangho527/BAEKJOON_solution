#A,B 입력 받은 후 A+B를 출력, 테스트 케이스 개수가 주어지고 테스트 케이스 번호는 1부터 시작

T = int(input())

for i in range(1,T+1):
    a,b=map(int,input().split())
    print("Case #{}: {}". format(i,a+b))