# 백준 - 카드 - 11652 - 자료 구조, 해시(dict), 정렬 문제
'''
자료 구조, 해시(dict), 정렬 문제

해시(파이썬에서는 딕셔너리)를 잘 활용하면 쉽게 풀 수 있는 문제이다.
n을 입력받고 n만큼 반복하면서 res 딕셔너리에 키가 있으면 + 1 없으면 1로 해서
출력할 때 밸류의 역순으로 먼저 정렬한 후 동일한 값이 있을 경우를 생각해서 키로 다시 정렬을 한 다음
처음 나오는 값을 출력하면 된다.

in
    5
    1
    2
    1
    2
    1
----------------
    6
    1
    2
    1
    2
    1
    2
out
    1
----------------
    1
'''

n = int(input())
res = dict()

for _ in range(n):
    a = int(input())
    
    if a in res:
        res[a] += 1
    else:
        res[a] = 1

print(sorted(res.items(), key=lambda x: (-x[1], x[0]))[0][0])
