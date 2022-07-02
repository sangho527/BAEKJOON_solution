T = int(input())
for i in range(1, T+1):
    a,b = map(int, input().split())
    #print("Case #" + str(i) + ":", a, "+", b, "=", a+b) // "case #" 출력, str(i), 문자열 반복문출력
    print(f'Case #{i}: {a} + {b} = {a+b}') 