# 백준 - 골드1 - 부분수열의 합 2 - 1208 - 이진 탐색, 구현, 중간에서 만나기(meet in the middle) 문제
'''
이진 탐색, 구현, 중간에서 만나기(meet in the middle) 문제


기존의 부분수열의 합 문제에서 응용을 더 해야 되는 문제이다.
문제를 푸는데 시간도 오래 걸리고 많이 헤맸었다.
중간에서 만나기(meet in the middle) 알고리즘을 잘 몰랐는데 이번 기회에 공부를 하게 된거 같다.

중간에서 만나기(meet in ter middle) 알고리즘 이란.
    한 개의 그룹으로 완전 탐색을 하지 못하는 경우 두 개의 그룹으로 나누어 탐색하여
    그 결과를 확인하여 시간을 줄이는 알고리즘이다. (ex : O(2^N) → O(2 * 2^(N/2))) => 2^40 -> 2^20 + 2^20 이게 더 빠르게 동작한다.

풀이 과정
1. input으로 주어지는 입력 조건으로 입력 받고, 수열이 들어올 때 해당 수열을 절반씩 쪼갠다.
2. 절반씩 쪼갠 주열을 combinations를 활용해서 새로운 조합? 수열? 리스트를 만들고 각각 정렬한다. (left, right).sort()
    2.1 리스트[: n // 2] -> 0으로 (left)
    2.2 리스트[n // 2 :] -> 해당 리스트의 길이 - 1로 (right)
    2.3 combinations를 활용해서 새로운 리스트를 만들 때 combinations의 총 합을 append해야 된다.
3. 절반으로 쪼갠 수열들의 인덱스를 확인하기 위한 left_idx, right_idx라는 이름으로 변수를 만들고 각각 '0, right리스트의 총 길이 - 1'으로 초기화한다.
4. left_idx는 left리스트의 길이를 안 넘고, right_idx는 0 작아지기 전까지 while 반복문을 실행한다.
    4.1 while 반복문을 진행하면서 temp 라는 변수에 left리스트의 left_idx의 값, right리스트의 right_idx의 값을 더한 상태로 담는다.
    4.2 해당 temp가 s와 같다면
        4.2.1 같은 값이 몇번 나올수 있는지 확인하기 위해 left_cnt, right_cnt 변수를 각각 1로 초기화한다.
        4.2.2 left_idx와 right_idx의 해당 값들을 각각 original_left_idx와 original_right_idx의 대입한다.
        4.2.3 left_idx와 right_idx의 값을 각각 1을 더하고 빼준다. -> temp가 s와 같은 시점에서 s와 같은 숫자가 있는지 확인하기 위해.(나중에 곱셈으로 사용)
        4.2.4 1이 증가한 left_idx와 1을 뺀 right_idx의 각각 리스트 값들이 original의 값과 같고, 리스트의 범위가 벗어나지 않는다면 cnt들을 증가시킨다.
        4.2.5 다 진행한 후, left_cnt의 값과 right_cnt의 값의 곱을 res에 더해준다.
    4.2 temp가 s보다 크거나 같으면 right_idx의 값을 1 감소시킨다.
    4.3 temp가 s보다 작다면 left_idx의 값을 1 증가시킨다.
5. 부분수열의 합 - 1182와 동일하게 s가 0이면 아무것도 뽑지 않는 경우를 제외하기 위해 1을 빼준다.
'''

from itertools import combinations as combi

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, s = 5, 0
# n_list = [-7, -3 ,-2 ,5, 8] # 1
# n, s = 1, 5
# n_list = [5] # 1
# n, s = 1, 2
# n_list = [1] # 0
# n, s = 5, 0
# n_list = [0,0,0,0,0] # 31

res = 0
n_list_1, n_list_2 = n_list[:n // 2], n_list[n // 2:]
left, right = [], []

for i in range(len(n_list_1) + 1):
    temp = combi(n_list_1, i)

    for j in temp:
        left.append(sum(j))
left.sort()

for i in range(len(n_list_2) + 1):
    temp = combi(n_list_2, i)

    for j in temp:
        right.append(sum(j))
right.sort()

left_idx, right_idx = 0, len(right) - 1

while left_idx < len(left) and right_idx >= 0:
    temp = left[left_idx] + right[right_idx]

    if temp == s:
        left_cnt, right_cnt = 1, 1
        original_left_idx, original_right_idx = left_idx, right_idx
        left_idx, right_idx = left_idx + 1, right_idx - 1

        while left_idx < len(left) and left[left_idx] == left[original_left_idx]:
            left_cnt += 1
            left_idx += 1

        while right_idx >= 0 and right[right_idx] == right[original_right_idx]:
            right_cnt += 1
            right_idx -= 1

        res += left_cnt * right_cnt

    elif temp >= s:
        right_idx -= 1
    else:
        left_idx += 1

print(res if s != 0 else res - 1)