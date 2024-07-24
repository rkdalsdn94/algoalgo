# 백준 - 실버5 - And the Winner Is... Ourselves! - 17509 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

풀이 과정
 1. 입력 값들을 입력 받고, 정렬한다.
 2. res, temp를 0으로 초기화한다.
 3. for문을 돌면서 temp에 lst의 첫번째 값만큼 더하고 res에 temp에 20을 곱한 값을 더한다.
 4. res를 출력한다.
'''

lst = sorted([list(map(int, input().split())) for _ in range(11)])

# 테스트
# lst = sorted([
#     [20, 1], [20, 0], [20, 3], [10, 0], [10, 0],
#     [10, 0], [30, 0], [30, 0], [30, 0], [20, 0],
#     [20, 10]
# ]) # 1360

res, temp = 0, 0

for i in range(11):
    temp += lst[i][0]
    res += temp + 20 * lst[i][1]

print(res)
