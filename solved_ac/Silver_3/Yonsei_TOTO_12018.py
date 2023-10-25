# 백준 - 실버3 - Yonsei TOTO - 12018 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

처음에 문제를 어렵게 생각해서 완전 탐색방식으로 전체를 돌면서 답을 구해야 되나 하면서 헤매다가 다음의 아이디어가 생각났다.
    1. 과목 수 만큼 미리 입력을 다 받아놓고, 미리 계산을 한 뒤 temp에 필요한 마일리지를 append 한다.
    2. temp를 정렬한 뒤 값을 꺼내면서 m이 0보다 크거나 같을 때까지 res를 추가한다.

신청한 사람과 수강 인원을 계산하는 방법으론 다음과 같다.
    p가 l보다 작으면 수강 가능한 인원이 모자른 상황이므로 1 마일리지만 사용해서 수업을 들을 수 있다.
    p가 l보다 크면 수강 신청한 인원 중 l번째의 값과 똑같은 값을 올리면 된다. (마일리지가 같은 경우 우선순위가 더 높음)
따라서, p_list를 정렬 후 p와 l의 값을 비교 한 뒤, p가 클 경우 p_list[p - l]의 값을 temp에 append 하면 된다.

마지막 res를 구할 때 m - i가 0보다 크다로만 하면 틀린다.

in
    5 76
    5 4
    36 25 1 36 36
    4 4
    30 24 25 20
    6 4
    36 36 36 36 36 36
    2 4
    3 7
    5 4
    27 15 26 8 14
out
    4

in        -> 질문 게시판에 있는 이 예제를 돌리다 0보다 크거나 같다 조건으로 바꿨다.
    3 2
    2 4
    36 36
    2 4
    36 36
    2 4
    36 36
out
    2
'''

n, m = map(int, input().split())
temp = []
res = 0

for _ in range(n):
    p, l = map(int, input().split())
    p_list = sorted(list(map(int, input().split())))

    if p < l:
        temp.append(1)
    else:
        temp.append(p_list[p - l])

for i in sorted(temp):
    if m - i >= 0:
        res += 1
        m -= i

print(res)

