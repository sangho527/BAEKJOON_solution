num_list = list(map(int, input().split()))
num_list.sort() #정렬
print(num_list[1]) #[0]이 첫번째기 때문에 리스트에서 2번째 숫자인 [1]을 출력한다.

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