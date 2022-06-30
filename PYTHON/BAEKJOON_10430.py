#나머지 문제

A, B, C = map(int, input().split())


#print((A+B)%C)
#print(((A%C) + (B%C))%C)
#print((A*B)%C)
#print(((A%C)*(B%C))%C)

print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C ,sep= '\n') # sep 파라미터를 사용해 출력값이 여러개인 경우 각 출력값 사이에 삽입할 문자를 지정