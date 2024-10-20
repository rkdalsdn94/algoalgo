# 백준 - 실버2 - F7 - 2790 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

제출할 때 PyPy3 또는 input을 stdin으로 받아야 시간초과가 나지 않는다.

풀이 과정
  1. n을 입력받고 n_list에 n개의 수를 입력받는다.
  2. n_list를 오름차순으로 정렬한다.
  3. n_list의 각 원소에 n을 더해준다. (이때 n부터 시작해서 1씩 감소 해야 됨)
  4. n_list의 최대값을 구한다.
  5. res, idx를 0으로 초기화한다.
  6. n_list의 값을 순회하면서 i(n_list를 순회) + idx가 max_num보다 크거나 같으면 res에 1을 더해준다.
  7. max_num보다 결과가 어떻든 idx에 1을 더해준다.
  8. 위 계산을 다 하고나서 res를 출력하면 된다.
'''

n = int(input())
n_list = sorted([int(input()) for _ in range(n)])

# 테스트
# n = 3
# n_list = sorted([8, 10, 9]) # 3
# n = 5
# n_list = sorted([15, 14, 15, 12, 14]) # 4

for i in range(n):
    n_list[i] += n
    n -= 1

max_num = max(n_list)
res, idx = 0, 0

for i in n_list:
    if i + idx >= max_num:
        res += 1

    idx += 1

print(res)
