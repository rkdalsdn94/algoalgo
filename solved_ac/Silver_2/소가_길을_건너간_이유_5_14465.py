# 백준 - 실버2 - 소가 길을 건너간 이유 5 - 14465 - 누적 합, 슬라이딩 윈도우 문제
'''
누적 합, 슬라이딩 윈도우 문제

처음 코드에선 res를 구하는 과정에서 i + k리스트의 0을 count 한다.
    - 이 부분 때문에 시간 초과가 나는거 같다. (제일 밑에 코드가 있음)
따라서 코드를 슬라이딩 윈도우 방식으로 수정하고 통과했다.

풀이 과정
 - n_list에서 고장난 신호등 부분을 0으로 바꿔야 한다. (이때 1을 빼야 됨)
 - 그 후 n_list의 0번째 인덱스 부터 k 번째 까지의 sum을 통해 window를 구하고, res를 k - window로 초기화한다.
 - 마지막으로 1부터 n - k + 1까지의 반복문으로 윈도우를 수정해가며 res를 더 작은 값으로 만들어 준다.
    - 조금이라도 더 빠르게 동작하게 만들기 위해 res가 0이면 더이상 작아질 수 없으므로 반복문을 종료한다.
 - 최종적으로 구한 res를 출력하면 된다.
'''

n, k, b = map(int, input().split())
b_list = [int(input()) for _ in range(b)]

# 테스트
# n, k, b = 10, 6, 5
# b_list = [2, 10, 1, 5, 9]

n_list = [1] * n
for i in b_list:
    n_list[i - 1] = 0

window = sum(n_list[:k])
res = k - window
for i in range(1, n - k + 1):
    window = window - n_list[i - 1] + n_list[i - 1 + k]
    res = min(res, k - window)
    if res == 0:
        break

print(res)

'''
시간 초과 코드

n, k, b = 10, 6, 5
b_list = [2, 10, 1, 5, 9]

n_list = [1] * n
for i in b_list:
    n_list[i - 1] = 0

res = int(1e9)
for i in range(n - k + 2):
    res = min(res, n_list[i:i + k].count(0)) # 이 부분에서 시간 초과가 날 거 같다.
    if res == 0:
        break

print(res)
'''
