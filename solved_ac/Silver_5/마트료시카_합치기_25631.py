# 백준 - 실버5 - 마트료시카 합치기 - 25631 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

n의 범위가 최대 1000까지 밖에 안돼서 단순하게 그리디한 방식으로 풀었다.

입력받은 마트료시카의 크기 리스트(n_list)에서 모든 배열을 순회하면서 같은 값이 있는지 count한 다음에 count 한 결과를 temp에 담는다.
max함수를 이용해 res를 res, temp에서 더 큰 값으로 바꿔준다.
res를 출력한다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 3
# n_list = sorted([1, 2, 3]) # 1
# n = 4
# n_list = sorted([2, 1, 4, 2]) # 2
# n = 7
# n_list = sorted([3, 3, 4, 5, 2, 2, 3]) # 3

res = 0

for i in range(n):
    temp = n_list.count(n_list[i])
    res = max(res, temp)

print(res)

