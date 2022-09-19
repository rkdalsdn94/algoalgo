# 백준 - 주몽 - 1940 - 실버4 - 정렬, 투 포인터 문제
'''
정렬, 투 포인터 문제

전에 풀었던 '두 수의 합 - 실버3 - 3273' 문제랑 똑같이 풀면 된다.
해당 문제에선 temp == m 일때 left 변수만 + 1 씩 했었는데, right 변수도 - 1 하는게 시간적으로 더 빠르게 동작했다.
다음에 비슷한 문제를 풀 때 참고해서 풀어야겠다.
'''

n = int(input())
m = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 6
# m = 9
# n_list = sorted([2, 7, 4, 1, 5, 3]) # 2

left, right = 0, n - 1

res = 0

while left < right:
    temp = n_list[left] + n_list[right]

    if temp == m:
        res += 1
        left += 1
        right -= 1
    elif temp < m:
        left += 1
    else:
        right -= 1

print(res)
