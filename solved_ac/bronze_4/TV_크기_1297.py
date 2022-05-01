d, h, w = map(int, input().split())

# 테스트
d, h, w = 52, 9, 16 # 25 45
d, h, w = 7, 2, 3 # 3 5
d, h, w = 13, 7, 10 # 7 10
d, h, w = 7, 32, 47 # 3 5

r = d / ((h ** 2 + w ** 2) ** 0.5)

print(int(h * r), int(w * r))