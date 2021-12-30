'''
    in으로 들어오는 값의 크기가 최대 1조가 넘어서 이 부분을 신경써야 함 (에라토스테네스의 체를 사용하면 괜찮을거 같다)
'''

def solution(x, y):
    res = y - x + 1
    prime_list= [False] * (y - x + 1)

    if x == 1 and y == 1:
        return 0

    for i in range(2, int(y ** 0.5 + 1)):
        temp = i ** 2

        for j in range((((x - 1) // temp) + 1) * temp, y + 1, temp):
            if prime_list[j - x] == False:
                prime_list[j - x] = True
                res -= 1

    return res

# x, y = map(int, input().split())
# print(solution(x, y))
print(solution(1, 10)) # 7
print(solution(15, 15)) # 1
print(solution(1, 1000)) # 608
print(solution(1, 1)) # 0