# 백준 - 실버3 - 블로그 - 21921 - 누적 합, 슬라이딩 윈도우 문제
'''
누적 합, 슬라이딩 윈도우 문제

처음에 sum을 사용해서 문제를 풀려고 했는데, sum 때문에 시간 초과가 나왔다.
당연하게도 sum 은 O(n) 의 복잡도를 가진다. 즉, for 문 안에서 sum 을 사용하면 n^2 의 복잡도로 인해 시간 초과가 나온다.
따라서, 다른 방법을 생각해야 된다. 이 부분을 슬라이딩 윈도우 방식으로 이용했다.

https://www.youtube.com/watch?v=uH9VJRIpIDY 여기 영상을 보면 코드는 슬라이딩 윈도우에 대해 설명이 있다. 이 영상을 참고해 구현하면 다음과 같다.

처음과 마지막만 바뀌고 가운데 부분은 중복해서 사용할 수 있다. 즉, n_list[i - x] 이 부분을 빼고, n_list[i] 부분을 더하면 윈도우가 바뀌는 것이다.
만약 다음과 같은 리스트가 있고 윈도우가 3이라면 [1,2,3,4,5,6]
    1 : [1,2,3]
    2 : [2,3,4] # 2, 3 이 위랑 겹친다.
    3 : [3,4,5] # 3, 4 가 위랑 겹친다.
        .
        .
        .
즉, list 에서 처음 부분을 빼고, 겹치는 부분은 냅두고, 그 뒤에 부분을 더하면 O(1) 만에 접근할 수 있다.
이 방식으로 풀면 된다.
'''

n, x = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, x = 5, 2
# n_list = [1, 4, 2, 5, 1]  # 7  \  1
# n, x = 7, 5
# n_list = [1, 1, 1, 1, 1, 5, 1]  # 9  \  2
# n, x = 5, 3
# n_list = [0, 0, 0, 0, 0]  # SAD

res, res_cnt = sum(n_list[:x]), 1
temp = res

if sum(n_list) == 0:
    print('SAD')
    exit(0)

for i in range(x, n):
    temp -= n_list[i - x] # 슬라이딩 윈도우 할 때 sum을 사용하면 안 된다.
    temp += n_list[i]

    if temp > res:
        res = temp
        res_cnt = 1
    elif temp == res:
        res_cnt += 1

print(res)
print(res_cnt)

'''
시간 초과 코드

n, x = map(int, input().split())
n_list = list(map(int, input().split()))

res, res_cnt = sum(n_list[:x]), 1

if sum(n_list) == 0:
    print('SAD')
    exit(0)

for i in range(1, n - x + 1):
    temp = sum(n_list[i:x + i]) # 여기 부분에서 sum 을 사용하면 시간 초가가 나온다. 

    if temp == res:
        res_cnt += 1
    elif temp > res:
        res = temp
        res_cnt = 1

print(res)
print(res_cnt)
'''
