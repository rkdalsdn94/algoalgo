# 백준 - 브론즈1 - 알고리즘 수업 버블 정렬 1 - 23968 - 구현, 정렬, 시뮬레이션 문제
'''
구현, 정렬, 시뮬레이션 문제

PyPy3로 제출해야 된다.

풀이 과정
  1. 버블 정렬을 구현한다.
  2. 버블 정렬을 수행하면서 수행될 때마다 카운트를 증가시킨다.
  3. 카운트가 k와 같아지면 해당 값을 출력하고 종료한다.
  4. 카운트가 k와 같아지지 않으면 -1을 출력한다.
'''

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 6, 10
# n_list = [4, 6, 5, 1, 3, 2] # 2 4
# n, k = 6, 12
# n_list = [4, 6, 5, 1, 3, 2] # -1

count = 0
res = -1

for i in range(n - 1, 0, -1):
    for j in range(i):
        if n_list[j] > n_list[j + 1]:
            count += 1
            n_list[j], n_list[j + 1] = n_list[j + 1], n_list[j]

            if count == k:
                res = f'{n_list[j]} {n_list[j+1]}'
                print(res)
                exit(0)

print(res)
