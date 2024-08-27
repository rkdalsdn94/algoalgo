# 백준 - 골드1 - 멀티탭 스케줄링 - 1700 - 그리디 문제
'''
그리디 문제

멀티탭을 뽑을 때 가장 나중에 사용할 것을 뽑는다면 가장 적은 횟수로 뽑을 수 있다.
따라서 가장 나중에 사용할 것을 뽑는다.

풀이 과정
    1. 입력을 받는다.
    2. 멀티탭을 뽑을 때 가장 나중에 사용할 것을 뽑는다.
    3. 뽑은 횟수를 출력한다.
'''

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 2, 7
# n_list = [2, 3, 2, 3, 1, 2, 7] # 2

plug = []
res = 0

for i in range(k):
    if n_list[i] in plug:
        continue
    if len(plug) < n:
        plug.append(n_list[i])
        continue

    temp = []
    for j in plug:
        try:
            temp.append(n_list[i:].index(j))
        except:
            temp.append(101)
    plug.pop(temp.index(max(temp)))
    plug.append(n_list[i])
    res += 1

print(res)
