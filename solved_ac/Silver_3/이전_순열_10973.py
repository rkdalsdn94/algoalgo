'''
구현, 수학, 조합론 문제

n = 3 일때
 ㄴ> 1 2 3
 ㄴ> 1 3 2
 ㄴ> 2 1 3
 ㄴ> 2 3 1
 ㄴ> 3 1 2
 ㄴ> 3 2 1
위와 같은 식으로 된다.

temp로 n_list를 정렬했을 때 같으면 -1을 출력하고 끝내면 된다.
그게 아니면 역순으로 돌면서 i가 i - 1보다 작고,
i - 1가 새로 시작하는 역순보다 작으면 j와 i - 1을 수홥 후
n_list를 새로 정렬한 후에 해당 n_list를 출력 후 종료하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# n = 4
# n_list = [1,2,3,4] # -1
# n = 5
# n_list = [5,4,3,2,1] # 5 4 3 1 2
# n = 3
# n_list = [2,1,3] # 1 3 2

temp = sorted(n_list)

if temp == n_list:
    print(-1)
    exit(0)

for i in range(n - 1, 0, -1):
    if n_list[i] < n_list[i - 1]:
        for j in range(n - 1, 0, -1):
            if n_list[j] < n_list[i - 1]:
                n_list[j], n_list[i - 1] = n_list[i - 1], n_list[j]
                n_list = n_list[:i] + sorted(n_list[i:], reverse=True)
                print(*n_list)
                exit(0)
