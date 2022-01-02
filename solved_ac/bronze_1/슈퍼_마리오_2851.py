def solution(mushroom_list):
    res = 0
    score = 0

    for i in mushroom_list:
        score += i

        if 100-res >= abs(100-score):
            res = score

    return res


mushroom_list = [int(input()) for _ in range(10)]
# print(mushroom_list)

print(solution(mushroom_list))
# print(solution([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # 100
# print(solution([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])) # 87
# print(solution([40, 40, 40, 40, 40, 40, 40, 40, 40, 40])) # 120
