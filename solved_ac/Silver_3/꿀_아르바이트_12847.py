# 백준 - 실버3 - 꿀 아르바이트 - 12847 - 누적 합, 슬라이딩 윈도우 문제
'''
누적 합, 슬라이딩 윈도우 문제

누적 합과, 슬라이딩 윈도우를 사용하면 되는 문제이다.
누적 합으로 처음에 0 ~ m까지의 합을 구하고, 슬라이딩 윈도우로 값을 빼고 더하면 된다.

풀이 과정
 - 입력으로 들어오는 n, m을 받고 n_list를 받는다.
 - 처음에 0 ~ m까지의 합을 temp에 저장하고 res에 저장한다.
 - start, end를 0, m으로 두고 end가 n보다 작을 때 까지 반복한다.
    - res와 temp 중 큰 값을 res에 저장한다.
    - temp에 start번째 값을 빼고 end번째 값을 더한다.
    - start, end를 1씩 증가시킨다.
 - res를 출력한다.
'''

n, m = map(int, input().split())
n_list = [0] + list(map(int, input().split()))

# 테스트
# n, m = 5, 3
# n_list = [0] + [10, 20, 30, 20, 10] # 70
# n, m = 5, 3
# n_list = [0] + [10, 20, 30, 0, 80] # 110

temp = sum(n_list[:m])
res = 0
start, end = 0, m

while end < n:
    res = max(res, temp)
    temp = temp - n_list[start] + n_list[end]
    start += 1
    end += 1

print(res)
