'''
그리디 문제이다.

처음에 어렵게 생각을 하다가 문제를 못 풀고 있었는데,
다른 반례가 생각이 나지 않아 문제 푼 그대로 제출했는데 통과였다.
내가 푼건 정렬을 한 후에 중간값을 구하고 그 값을 출력하는거 였다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 4
# n_list = sorted([5,1,7,9]) # 5

res = n_list[(n-1) // 2]

print(res)
