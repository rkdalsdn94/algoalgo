# 백준 - 실버3 - 현대모비스 입사 프로젝트 - 27922 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

풀이 과정
    1. 입력을 받는다.
    2. temp_12, temp_23, temp_13을 만들어 각각의 값을 정렬한다.
    3. res를 만들어 각각의 값을 더해준다.
    4. res 중 가장 큰 값을 출력한다.
'''

n, k = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, k = 3, 2
# n_list = [[2, 4, 10], [55, 8, 2], [1, 9, 5]] # 73

temp_12 = sorted(n_list, key=lambda x: -(x[0] + x[1]))
temp_23 = sorted(n_list, key=lambda x: -(x[1] + x[2]))
temp_13 = sorted(n_list, key=lambda x: -(x[0] + x[2]))

res = [0] * 3

for i in range(k):
    res[0] += temp_12[i][0] + temp_12[i][1]
    res[1] += temp_13[i][0] + temp_13[i][2]
    res[2] += temp_23[i][1] + temp_23[i][2]

print(max(res))
