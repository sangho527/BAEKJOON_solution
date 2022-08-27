k, n, m = list(map(int, input().split()))

print(((k*n)-m) if ((k*n)-m) >= 0 else 0) # 가진돈 - (과자개수 * 과자가격) 