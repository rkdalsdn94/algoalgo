# 백준 - 실버2 - 숨바꼭질 6 - 17087 - 수학, 정수론, 유클리드 호제법 문제
'''
수학, 정수론, 유클리드 호제법 문제

처음에 문제를 정확히 이해하지 않은 상태테서 최소 거리를 구하는 문제구나 했다가 틀렸다.
문제의 핵심은 다음과 같다. '모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.'
즉, 모든 동생을 찾기위한 값을 구해야 된다. 이 부분을 gcd로 구하는 문제이다.

풀이 과정
 - 동생들의 인원수인 n과 수빈이의 위치 s 를 입력받은 뒤, a_list 라는 이름으로 동생들의 위치를 입력받는다.
 - 수빈이의 위치와 동생들의 거리 차를 알기 위해 distance 라는 이름의 배열로 두 거리의 차를 구한다.
    - 이때 동생의 위치는 모두 다르며, 수빈이의 위치와 같지 않다는 조건이 있으므로 그냥 abs 함수를 통해 s - i의 차를 append 하면 된다.
 - res를 distance의 0번째 인덱스 값으로 초기화한 뒤 나머지 값을 gcd 함수를 이용해 답을 구하면 된다.
'''

from math import gcd

n, s = map(int, input().split())
a_list = list(map(int, input().split()))

# 테스트
# n, s = 3, 3
# a_list = [1, 7, 11] # 2
# n, s = 3, 81
# a_list = [33, 105, 57] # 24
# n, s = 1, 1
# a_list = [1000000000] # 999999999

distance = []
for i in a_list:
    distance.append(abs(s - i))

res = distance[0]
for i in range(1, n):
    res = gcd(res, distance[i])

print(res)
