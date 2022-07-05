hour, minute = map(int, input().split())
add = int(input())

hour1 = ((hour)+(minute+add)//60)%24
minute1 = (minute+add)%60

print(hour1, minute1)


#(hour + ((minute + add)//60)) % 24