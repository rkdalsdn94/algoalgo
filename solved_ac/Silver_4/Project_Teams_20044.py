# 백준 - 실버4 - Project Teams - 20044 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

입력받은 리스트를 정렬 후 각 인덱스의 반대의 값끼리 더한다.
    (ex. 0번째 인덱스 + 마지막 인덱스, 1번째 인덱스 + 마지막 전 인덱스 이런식)
위의 방법으로 구한 값 중 제일 작은 값을 출력하면 되는 문제이다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 2
# n_list = sorted([1, 7, 5, 8]) # 9
# n = 3
# n_list = sorted([1, 7, 3, 5, 9, 2]) # 8

res = []
for i in range(1, n + 1):
    res.append(n_list[i - 1] + n_list[-i])

print(min(res))
