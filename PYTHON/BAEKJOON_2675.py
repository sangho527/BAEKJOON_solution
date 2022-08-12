t = int(input())
for i in range(t):
    num, s = input().split() #문자열을 입력받고 줄 바꿈
    text = ''
    for i in s: #반복문
        text += int(num) * i
    print(text)