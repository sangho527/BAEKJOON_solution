dish = list(str(input())) # 리스트에 넣어서 저장
answer = 0

for i in range(len(dish)): #for문 사용
    if i == 0:
        answer += 10
    elif dish[i] == dish[i-1]:
        answer += 5
    else:
        answer += 10
        
print(answer) 