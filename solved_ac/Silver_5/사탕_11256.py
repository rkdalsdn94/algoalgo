# 백준 - 실버5 - 사탕 - 11256 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

풀이 과정
1. 상자의 수(n)만큼 반복하면서 상자의 세로와 가로 길이의 곱을 n_list에 담는다. 다 담은 후에는 내림차순으로 정렬한다.
2. temp 변수를 만들어 0으로 초기화 한 후 temp가 j보다 작을때만 실행할 수 있는 while문을 만든다.
3. 내림차순으로 정렬된 n_list의 값들을 하나 씩 꺼내가며 temp에 더해준다.
    3.1 위 과정을 한 번씩 진행할 때마다 res에 1을 더해준다.
4. temp가 j의 값과 같거나 커지는 순간 while문을 종료한 후 res를 출력하면 된다.
'''

t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    n_list = []

    for _ in range(n):
        a, b = map(int, input().split())
        n_list.append(a * b)

    n_list.sort(reverse=True)
    res = 0
    temp = 0

    while temp < j:
        temp += n_list.pop(0)
        res += 1

    print(res)
