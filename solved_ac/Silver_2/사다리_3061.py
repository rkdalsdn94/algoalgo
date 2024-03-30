# 백준 - 실버2 - 사다리 - 3061 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

처음에 답을 어떻게 구해야 되는지 고민을 꽤 한 문제이다.
그러다 질문 게시판에서 정렬을 사용한다는 걸 보고 알 수 있었다.
즉, 앞에 있는 값이 뒤에 있는 값보다 크다면 res를 1씩 증가하면 된다.

풀이 과정
 - 입력을 잘 받고, 도착하는 사다리(n_list)를 정렬이 필요한 순간마다 res를 1씩 더한 뒤 출력하면 된다.

in
    2
    4
    3 2 4 1
    3
    3 1 2
out
    4
    2
'''

t = int(input())
for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if n_list[i] > n_list[j]:
                res += 1

    print(res)
