a = int(input())
b = input()
b1 = int(b[2]) # 일의 자리
b2 = int(b[1]) # 십의 자리
b3 = int(b[0]) # 백의 자리
axb = a * int(b)

print(a*b1, a*b2, a*b3 ,axb ,sep='\n')