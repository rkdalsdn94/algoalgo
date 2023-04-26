# 백준 - 실버2 - MVP 다이아몬드 Easy - 20413 - 그리디 문제
'''
그리디 문제

문제에 '만원 단위로'와 최대 금액을 구하는 것이라 grade_score 의 각 원소에서 1을 뺀 값을 res에 더해주면 된다.
grade_list를 한 글자씩 돌면서 해당 tier의 점수를 1과 temp(이전 값)을 빼고, res에 더하면 된다.
'''

n = int(input())
tier_score = list(map(int, input().split()))
grade_list = input()

# 테스트
# n = 3
# grade_score = [ 30, 60, 90, 150 ]
# grade_list = 'BSG' # 118
# n = 10
# grade_score = [ 257, 269, 367, 500 ]
# grade_list = 'BSGGGGPPDD' # 2499

res, temp = 0, 0

for i in range(n):
    if grade_list[i] == 'B':
        res += tier_score[0] - 1 - temp
        temp = tier_score[0] - 1 - temp
    elif grade_list[i] == 'S':
        res += tier_score[1] - 1 - temp
        temp = tier_score[1] - 1 - temp
    elif grade_list[i] == 'G':
        res += tier_score[2] - 1 - temp
        temp = tier_score[2] - 1 - temp
    elif grade_list[i] == 'P':
        res += tier_score[3] - 1 - temp
        temp = tier_score[3] - 1 - temp
    elif grade_list[i] == 'D':
        res += tier_score[3]
        temp = tier_score[3]

print(res)
