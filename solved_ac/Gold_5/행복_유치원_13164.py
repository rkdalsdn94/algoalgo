# 백준 - 골드5 - 행복 유치원 - 13164 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

핵심 아이디어
    - 키 차이를 기준으로 정렬하여 차이가 큰 순서대로 K - 1개의 차이를 더한다.
    - K개의 그룹으로 나누기 위해 K-1개의 차이에서 가장 큰 차이를 제외한 나머지 차이들의 합 출력한다.

풀이 과정
    1. N, K를 입력받는다.
    2. 키를 입력받고 차이를 계산한다.
    3. 차이를 기준으로 정렬한다.
    4. 차이가 큰 순서대로 K-1개의 차이를 더한다.
    5. 결과를 출력한다.
'''

n, k = map(int, input().split())
heights = list(map(int, input().split()))

# 테스트
# n, k = 5, 3
# heights = [1, 3, 5, 6, 10]  # 3

res = []
for i in range(1, n):
    res.append(heights[i] - heights[i-1])

res.sort(reverse=True)
print(sum(res[k - 1:]))
