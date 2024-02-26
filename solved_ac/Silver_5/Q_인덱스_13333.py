# 백준 - 실버5 - Q 인덱스 - 13333 - 완전 탐색, 정렬 문제
'''
완전 탐색, 정렬 문제

단순히 정렬 후 n부터 -1까지 내려오면서 이 값과 해당 인덱스의 값과 비교하면 되는 문제이다.

풀이 과정
 - 정렬 후 n의 값부터 -1까지 역순으로 내려가면서, 해당 인덱스의 값이 i의 값보다 크거나 같다면 반복문을 종료하고, i를 출력하면 된다.
    - 단, 이때 n_list의 인덱스를 찾을 때 '-' 붙여야 된다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 5
# n_list = sorted([8, 4, 5, 3, 10]) # 4
# n = 4
# n_list = sorted([0, 0, 0, 0]) # 0
# n = 6
# n_list = sorted([12, 7, 6, 8, 9, 10]) # 6

for i in range(n, -1, -1):
    if i <= n_list[-i]:
        print(i)
        break
