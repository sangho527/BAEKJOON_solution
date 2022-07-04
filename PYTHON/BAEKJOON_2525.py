#오븐 시계, 요리를 시작하는 시각과 요리를 하는데 필요한 시간이 분 단위로 주어졌을 때, 요리가 끝나는 시간을 계산하는 프로그램을 만들자.
#"""import time

#now = time.localtime()
#print('%02d %02d' %(now.tm_hour, now.tm_min))

#a = map(int,input().split())

#print('%02d %02d' %(now.tm_hour+a, now.tm_min+a))"""

hour, minute = map(int, input().split())
add = int(input())

h = (hour + ((minute + add)//60)) % 24
m = (minute + add) % 60 

print(h,m)