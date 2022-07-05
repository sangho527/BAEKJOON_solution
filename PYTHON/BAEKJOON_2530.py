#인공지능 시계 초단위 입력

hour, minute, sec = map(int, input().split())

add = int(input())
hour1 = (hour + (minute+((sec+add)//60))//60)%24
minute1 = (minute+((sec+add)//60))%60
sec1 = (sec+add)%60

print(hour1, minute1, sec1) 


# ((sec+add)%60) = 몫은 101 나머지는 0
#hour1 = hour + (minute+((sec+add)%60))//24 // 은 몫 %는 나머지