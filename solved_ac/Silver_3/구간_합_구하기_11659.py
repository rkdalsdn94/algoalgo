'''
누적 합, 단순 구현 문제
in
    5 3
    5 4 3 2 1
    1 3
    2 4
    5 5
out
    12
    9
    1

input을 sys.stdin.readline 이걸로 해야 통과다. (입력 값이 많아서 읽는데 시간이 걸리는거 같다, n과 m이 최대 10만)
구하는건 단순한데 sum을 활용하면 n^2이 된다. 그래서 누적 합을 구한 다음에(첫 번째 for문에서 res)
res를 이용해서 누적 합끼리의 뺄셈을 하면 된다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m_list = [0] + list(map(int, input().split()))
res = []
temp = 0

for i in range(len(m_list)):
    temp += m_list[i]
    res.append(temp)

for _ in range(m):
    a, b = map(int, input().split())
    print(res[b] - res[a - 1])
