# 백준 - 실버3 - 모두의 마블 - 12845 - 그리디 문제
'''
그리디 문제

내림차순으로 정렬한 뒤에 0번째와 1번째의 값을 res에 담은 후, 나머지 n_list의 값을 2부터 0번째 인덱스와 더해주면 된다.
문제 설명이 오히려 더 까다롭게 만든 문제인거 같다. 문제를 푸는 시간보다 이해하는 데 시간이 더 걸렸다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())), reverse=True)

# 테스트
# n = 3
# n_list = [40, 30, 30] # 140

res = n_list[0] + n_list[1]

for i in range(2, n):
    res += n_list[0] + n_list[i]

print(res)
