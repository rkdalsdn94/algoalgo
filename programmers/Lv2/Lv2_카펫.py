def solution(brown, yellow):
    for i in range(yellow, 0, -1):
        if yellow % i == 0:
            x = i
            y = yellow // i
            if (x+2) * 2 + y*2 == brown:
                return [x+2, y+2]


print(solution(10, 2))  # [4,3]
print(solution(8, 1))  # [3,3]
print(solution(24, 24))  # [8,6]
