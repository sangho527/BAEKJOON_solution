num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[1])

"""a, b, c = map(int, input().split(' '))

if(a >= b):
    if(a >= c):
        if(b >= c):
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if(b >= c):
        if(a >= c):
            print(a)
        else:
            print(c)
    else:
        print(b)""" #if문 사용