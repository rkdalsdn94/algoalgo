a, b = 0, 1
for _ in range(int(input())):
    a, b = b % 15746, (a + b) % 15746
print(b)

# input : 4 - out : 5
# 그냥 피보나치 문제임
# 처음에 마지막에서만 % 15746 이걸 했는데 시간초과남.. 속도가 느림..