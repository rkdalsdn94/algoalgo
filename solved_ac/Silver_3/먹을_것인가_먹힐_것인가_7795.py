# 백준 - 먹을 것인가 먹힐 것인가 - 실버3 - 정렬, 이진 탐색, 투 포인터 문제
'''
정렬, 이진 탐색, 투 포인터 문제

처음에 완전 탐색 방식으로 문제를 풀려고 했는데 시간 초과가 나왔다. (PyPy3로 하거나 같은 방식으로 c++로 제출하면 가능)

그래서 이진 탐색 방식으로 바꾼 다음 문제를 푸니까 시간 걱정없이 통과할 수 있었다.

풀이 과정
1. a_list의 원소들을 순서대로 반복한다.
2. temp는 -1, start는 0, end는 b_list 길이의 - 1(m)으로 초기화 시킨다.
3. start가 end와 작거나 같을 동안 반복문을 실행한다.
4. mid(b_list의 index 용도)를 설정해 준 후 b_list의 mid번째 인덱스가 i(현재 반복하고 있는 a_list의 원소)보다 작은지 비교한다.
    4.1 b_list[mid]가 i보다 작으면 temp는 mid 값으로 바꾸고 start + 1을 진행한다.
    4.2 b_list[mid]가 i보다 크면 end 값을 -1을 한 후에 이 전 인덱스도 작은지 검사한다.
5. start값이 end값보다 커지면 res에 temp값을 더하고 출력하면 된다.

in
    2
    5 3
    8 1 7 3 1
    3 6 1
    3 4
    2 13 7
    103 11 290 215
out
    7
    1
'''

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a_list = sorted(map(int, input().split()))
    b_list = sorted(map(int, input().split()))
    res = 0

    for i in a_list:
        start, end = 0, m - 1
        temp = -1

        while start <= end:
            mid = (start + end) // 2

            if b_list[mid] < i:
                temp = mid
                start = mid + 1
            else:
                end = mid - 1
        res += temp + 1

    print(res)

'''
완전 탐색으로 풀기
시간 초과 코드 (PyPy3로 제출하면 통과할 수 있다.) 아래와 같은 방식으로 c++로 하면 통과할 수 있다.


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a_list = sorted(list(map(int, input().split())), reverse=True)
    b_list = sorted(list(map(int, input().split())))
    res = 0
    
    for i in a_list:
        for j in b_list:
            if i > j:
                res += 1
            else:
                break

    print(res)
'''