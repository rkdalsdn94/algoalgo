# 백준 - 실버3 - 삼각형 만들기 - 수학, 그리디, 정렬 문제
'''
수학, 그리디, 정렬 문제

해당 문제를 풀기 전에 '삼각형 결정조건'의 부분을 알고 있어야 풀 수 있다.
'삼각형의 결정조건'을 모른다면 여기 링크에서 읽어보면 도움이 된다. https://mathbang.net/92
  - 위 링크에서 보면 3변의 길이가 주어질 때 삼각형을 만들고자 한다면,
  - 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 작아야지 삼각형을 만들 수 있다.

이 문제에선 세 변의 길이가 가장 긴 값을 출력해야 하므로
n_list의 값들을 내림차순으로 정렬을 한 다음에 '삼각형의 결정조건'을 만족할 때 break를 하고, res를 출력 하면 된다.
'''

import sys; input = sys.stdin.readline

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ], reverse=True)

# 테스트
# n = 3
# n_list = sorted([1,2,3], reverse=True) # -1
# n = 3
# n_list = sorted([1,2,2], reverse=True) # 5
# n = 6
# n_list = sorted([2, 3, 2, 3, 2, 4], reverse=True) # 10
# n = 5
# n_list = sorted([4, 5, 6, 7, 20], reverse=True) # 18

res = -1

for i in range(n - 2):
    if n_list[i] < n_list[i + 1] + n_list[i + 2]: # 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 작아야 한다.
        res = sum(n_list[i:i + 3])
        break

print(res)
