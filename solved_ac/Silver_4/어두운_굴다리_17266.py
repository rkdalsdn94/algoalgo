# 백준 - 실버4 - 어두운 굴다리 - 17266 - 이분 탐색, 구현, 스와핑 문제
'''
이분 탐색, 구현, 스와핑 문제

문제 분류샹에는 이분 탐색으로 되어있는데 어떻게 풀어야 될지 도저히 감이 안온다 (다른 사람들의 풀이를 봐도 이해가 잘 안 된다... 계속 보면 됐었는데..)
아래 코드로 푼 방식은 빛을 비추는 중간값과 양 끝까지의 값 중 가장 큰 값을 찾는 방식으로 풀었다.
https://devlibrary00108.tistory.com/508 여기 코드를 보고그림을 많이 그려보면서 이해했다.

공부를 더 한 뒤에 이분 탐색으로 다시 풀어봐야 될 거 같다.
'''

n, m = int(input()), int(input())
x_list = list(map(int, input().split()))

# 테스트
# n, m = 5, 2
# x_list = [2, 4] # 2
# n, m = 3, 1
# x_list = [0] # 3

res = 0
for i in range(1, m):
    res = max(res, x_list[i] - x_list[i - 1])

print(max((res + 1) // 2, x_list[0] - 0, n - x_list[-1]))
