x_ = []
y_ = []
for i in range(3):
        x, y = map(int, input().split())
        x_.append(x) #append 덧붙이다
        y_.append(y)
for i in range(3):
        if x_.count(x_[i]) == 1: #요소의 개수를 세서 개수가 하나인 것을 출력
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)