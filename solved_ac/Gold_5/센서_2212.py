# 백준 - 골드5 - 센서 - 2212 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

입력으로 들어온 센서들의 좌표를 정렬한 뒤, 각 거리의 차를 res에 담는다.
res를 내림차순으로 정렬한 후 집중국의 - 1 만큼 res의 제일 큰 값을 pop한다.
    ㄴ> k개의 구간으로 나눠야 된다. 즉, k가 2일 때 리스트를 한 번 자르면 2게의 구간이 되므로 -1을 해야 된다.
res의 전체 합을 출력하면 된다.
'''

n = int(input())
k = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 6
# k = 2
# n_list = sorted([1,6,9,3,6,7]) # 5
# n = 10
# k = 5
# n_list = sorted([20,3,14,6,7,8,18,10,12,15]) # 7

res = []
for i in range(1, n):
    res.append(n_list[i] - n_list[i - 1])

res.sort(reverse=True) # 내림차순으로 정렬한 뒤
for _ in range(k - 1): # 집중국을 세워서 거리의 차가 큰 부분을 분류한다.
    if res: # 이 부분이 없어서 처음에 인덱스 에러가 발생했다.
        res.pop(0)

print(sum(res))
