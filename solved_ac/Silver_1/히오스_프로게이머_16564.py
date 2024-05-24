# 백준 - 실버1 - 히오스 프로게이머 - 16564 - 이진 탐색, 매개 변수 탐색 문제
'''
이진 탐색, 매개 변수 탐색 문제

이진 탐색 문제이다. 이 전에 이진 탐색을 풀었었던 방식대로 비슷하게 풀면 된다.
단, start와 end를 설정할 때 주의해야 한다.
start는 n_list의 최솟값, end는 n_list의 최솟값 + k로 설정한다.
만약 21%에서 틀리면, start와 end를 잘 설정했는지 확인해보면 된다.

풀이 과정
 1. 입력을 받고, n_list를 입력받는다.
 2. 이진 탐색을 이용하여 최대값을 찾는다.
    2.1. start와 end를 설정하고, mid를 계산한다.
    2.2. temp를 0으로 초기화하고, n_list를 돌면서 mid보다 작은 경우 temp에 mid - i를 더한다.
    2.3. temp가 k보다 작거나 같은 경우 start를 mid + 1로 설정하고, res와 mid 중 큰 값을 res에 저장한다.
    2.4. temp가 k보다 큰 경우 end를 mid - 1로 설정한다.
 3. 최대값을 출력한다.
'''

n, k = map(int, input().split())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n, k = 3, 10
# n_list = [10, 20, 15]  # 17

res = 0
start, end = min(n_list), min(n_list) + k

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in n_list:
        if i < mid:
            temp += mid - i

    if temp <= k:
        start = mid + 1
        res = max(res, mid)
    else:
        end = mid - 1

print(res)
