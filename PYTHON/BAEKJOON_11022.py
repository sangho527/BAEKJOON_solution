t = int(input())

for X in range(1, t+1):

    a, b = map(int, input().split())
    c = a+b
    print(f'Case #{X}: {a} + {b} = {c}') # fstring 사용