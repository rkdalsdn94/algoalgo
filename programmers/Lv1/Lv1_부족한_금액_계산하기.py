# 문제 잘 읽기 -- 단, 금액이 부족하지 않으면 0을 return 하세요.

def solution(price, money, count):
    answer = money - sum([price * i for i in range(1, count+1)])
    if answer > 0:
        return 0
    return abs(answer)
print(solution(3, 20, 4)) # 10
