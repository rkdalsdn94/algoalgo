# 백준 - 골드5 - 용액 - 2467 - 투 포인터, 이분 탐색 문제
'''
투 포인터, 이분 탐색 문제

주의 사항으론 다음과 같다.
INF를 초기화할 때 int(1e9)로 하면 28%에서 틀린다.
문제를 보면 다음과 같다.
    -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 서로 다르고,
    '산성 용액만'으로나 '알칼리성 용액만'으로 입력이 주어지는 경우도 있을 수 있다.

즉, 입력이 이렇게 두 수로 주어질 때 [999_999_999, 1_000_000_000]
위 두 수의 값이 int(1e9)보다 더 크므로 최초 INF를 초기화할 때 양의 무한대 값인 float('inf')를 이용해야 한다.

풀이 과정
left, right를 이용한 투 포인터 방식으로 풀었다.
각각의 포인트를 배열의 시작 인덱스와 끝 인덱스에 위치시켜 놓는다.
두 인덱스 값의 합을 temp라는 이름에 담아놓고, 이 값을 이용해 다음의 비교를 진행한다.
    - abs(temp)가 INF 보다 작거나 같을 경우 0에 가까워 진 상황이므로 해당 인덱스들의 값을 정답으로 출력할 left_res, right_res에 담는다.
    - INF를 abs(temp) 값으로 변경한다.

위 과정을 진행한 후, temp가 0보다 작거나 같으면 0에 더 가깝게 하기 위해 left를 1 증가시키고,
마찬가지로 0보다 크면 0으로 더 가깝게 가기 위해 right에서 1을 빼면 된다.
이 과정을 left의 값이 right의 값보다 작을 때 까지만 반복한다. (두 인덱스의 값이 같아지면 안 됨)
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [-99, -2, -1, 4, 98] # -99, 98
# n = 4
# n_list = [-100, -2, -1, 103] # -2 -1

left, right = 0, n - 1
left_res, right_res = 0, 0
INF = float('inf') # int(1e9)로 했다가 틀린다. 입력으로 들어오는 값이 int(1e9)보다 더 큰 값이 생길 수 있음

# 투 포인터 풀이
while left < right: # 두 인덱스의 값이 같으면 안 된다. (left <= right 를 사용하면 안 됨, '=' 제거)
    temp = n_list[left] + n_list[right]

    if abs(temp) <= INF:
        left_res, right_res = n_list[left], n_list[right]
        INF = abs(temp)

    if temp <= 0:
        left += 1
    else:
        right -= 1
print(left_res, right_res)
