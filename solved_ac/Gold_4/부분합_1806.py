# 백준 - 골드4 - 부분합 - 1806 - 누적 합, 투 포인터 문제
'''
누적 합, 투 포인터 문제

투 포인터를 활용해서 문제를 풀어야 한다. 근데, while 문의 조건을 start <= end 으로 하면 안되고, 종료 조건을 따로 설정해야 된다.
종료 조건은 end 가 n 이랑 같아졌을 때이다. 이유는 list를 끝까지 방문한 것이므로 더 확인할 필요가 없다.
start 와 end 를 더하는 조건은 temp 가 s보다 크거나 같을 땐 start를 더하고, 작으면 end를 1을 더한다.
각 start와 end 의 값들을 temp에 담고 s와 비교하면 된다.
결국 res를 구하는게 가장 중요한 문제라 int(1e9)의 값으로 초기화한 상태에서 end - start + 1 두 값중 더 작은 값으로 변경하면 된다.
'''

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, s = 10, 15
# n_list = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8] # 2
# n, s = 10, 10
# n_list = [1,1,1,1,1,1,1,1,1,10] # 1

temp, res = n_list[0], int(1e9)
start, end = 0, 0

while 1:
    if temp >= s:
        res = min(res, end - start + 1)
        temp -= n_list[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        temp += n_list[end]

if res == int(1e9):
    print(0)
else:
    print(res)
