n = int(input()) # n입력 받고
i = 2
while n!=1: # n이 1과 같지 않다.
    if n%i == 0: 
        print(i)
        n = n/i
    else:
        i+=1