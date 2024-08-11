# 백준 - 실버3 - 게으른 백곰 - 10025 - 누적 합, 투 포인터, 슬라이딩 윈도우 문제
'''
누적 합, 투 포인터, 슬라이딩 윈도우 문제

풀이 과정
    1. 입력을 받는다.
    2. n_list를 받는다.
    3. n_list를 물의 양을 기준으로 오름차순으로 정렬한다.
    4. res, left, right, temp를 0으로 초기화한다.
    5. right가 n보다 작을 때까지 다음을 반복한다.
        5.1. n_list[right][1] - n_list[left][1]이 k * 2보다 작거나 같을 때
            5.1.1. temp에 n_list[right][0]을 더한다.
            5.1.2. res와 prefix_sum 중 큰 값을 res에 저장한다.
            5.1.3. right에 1을 더한다.
        5.2. n_list[right][1] - n_list[left][1]이 k * 2보다 클 때
            5.2.1. temp에서 n_list[left][0]을 뺀다.
            5.2.2. left에 1을 더한다.
    6. res를 출력한다.
'''

n, k = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, k = 4, 3
# n_list = [[4, 7], [10, 15], [2, 2], [5, 1]] # 11

n_list.sort(key=lambda x: x[1])

res = 0
left, right = 0, 0
prefix_sum = 0

while right < n:
    if n_list[right][1] - n_list[left][1] <= k * 2:
        prefix_sum += n_list[right][0]
        res = max(res, prefix_sum)
        right += 1
    else:
        prefix_sum -= n_list[left][0]
        left += 1

print(res)
