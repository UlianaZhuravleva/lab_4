data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
data = list(sorted(data, key = lambda x: abs(x)))
print(data)