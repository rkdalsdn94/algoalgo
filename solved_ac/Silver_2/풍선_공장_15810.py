# 백준 - 실버2 - 풍선 공장 - 15810 - 이진 탐색, 매개 변수 탐색 문제
'''
이진 탐색, 매개 변수 탐색 문제

이분 탐색으로 푸는건 알았는데 end와 while문 안에서 temp를 어떤 값을 기준으로 잡을지가 중요하다.

풀이 과정
 - 이진 탐색을 할 때 처음 end 값으로는 풍선을 만드는 시간들 중에서 제일 작은 값으로 m번 만드는 값이 end 값으로 설정한다.
 - temp(풍선의 갯수) 값은 mid 값을 n_list로 나눈 몫 값으로 더해준 뒤,
    이 풍선의 갯수가 m보다 작으면 start를 mid + 1로 바꾸고 res를 start 값으로 만든다.
 - 위 과정을 start가 end 값보다 커질 때까지 반복하면서 답글 구하면 된다.
'''

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, m = 3, 8
# n_list = [5, 7, 3] # 14

start, end = 0, min(n_list) * m
res = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in range(n):
        temp += mid // n_list[i]

    if temp < m:
        start = mid + 1
        res = start
    else:
        end = mid - 1

print(res)
