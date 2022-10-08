# 백준 - 골드4 - 집합의 표현 - 1717 - 자료 구조, 분리 집합, Union-Find 문제
'''
자료 구조, 분리 집합, Union-Find 문제

union-find 알고리즘을 써서 문제를 풀었다.
'서로소 집합(Disjoint-Set)'또는 '합집합 찾기'에 관련된 문제들은 union-find 알고리즘 사용해서 구현하는게 편하다.

m의 길이만큼 연산이 주어지니까 m_list라는 이름으로 연산을 미리 입력 받았다.
m_list의 첫 번째 인자가 0일 때는 union 시켜주고, 1일 때는 b와 c가 같은 부모인지를 체크 한다.
  - union 시켜줄 땐 n_list(부모)의 값이 더 작은 값으로 변경시켰다.
같은 부모(n_list의 값이 같다면..)이면 'YES' 아니면 'NO'를 출력하면 된다.
  - 같은 부모인지 찾는 방법은 find 함수를 이용해서 재귀적으로 확인하면 된다.

Gold_4/최소_스패닝_트리_1197.py 해당 파일 상단에 보면 Union-Find에 대해 관련된 링크가 있다. 해당 링크를 참고하면 된다.
'''
import sys; sys.setrecursionlimit(10 ** 9);

n, m = map(int, input().split())
m_list = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 7, 8
# m_list = [ [0,1,3], [1,1,7], [0,7,6], [1,7,1], [0,3,7], [0,4,2], [0,1,1], [1,1,1] ] # NO  NO  YES

n_list = [ i for i in range(n + 1) ]

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        n_list[b] = a
    else:
        n_list[a] = b

def find(x):
    if x != n_list[x]:
        n_list[x] = find(n_list[x])

    return n_list[x]

for i in m_list:
    a, b, c = i

    if a == 0:
        union(b, c)
    elif a == 1:
        temp_b = find(b)
        temp_c = find(c)

        if temp_b == temp_c:
            print('YES')
        else:
            print('NO')
