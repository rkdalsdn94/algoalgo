# 백준 - 골드5 - 숫자고르기 - 2668 - 그래프 이론, 그래프 탐색, dfs 문제
'''
그래프 이론, 그래프 탐색, dfs 문제

풀이 과정
    1. 입력을 받고, n_list를 만든다. (인덱스를 1부터 시작하기 위해 0을 추가한다.)
    2. 결과를 저장할 res를 만든다.
    3. dfs 함수를 정의하고, 각 노드에 대해 dfs를 실행한다.
        3.1. 방문한 노드는 ck를 True로 바꾼다.
        3.2. temp에 n_list[x]를 저장한다.
        3.3. temp가 방문하지 않은 노드라면 dfs를 실행한다.
        3.4. temp가 방문한 노드이고, temp가 i와 같다면 res에 추가한다.
    4. res를 출력한다.
'''

n = int(input())
n_list = [0] + [int(input()) for _ in range(n)]

# 테스트
# n = 7
# n_list = [0] + [3, 1, 1, 5, 5, 4, 6] # 3  \  1  \  3  \  5

res = []

def dfs(x, i):
    ck[x] = True
    temp = n_list[x]

    if not ck[temp]:
        dfs(temp, i)
    elif ck[temp] and temp == i:
        res.append(temp)

for i in range(1, n + 1):
    ck = [False] * (n + 1)
    dfs(i, i)

print(len(res))
for i in sorted(res):
    print(i)
