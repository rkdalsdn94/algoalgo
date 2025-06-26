# 백준 - 실버4 - 식당 메뉴 - 26043 - 자료구조(큐), 정렬 문제
"""
자료구조(큐), 정렬 문제

PyPy3 또는 input을 input=sys.stdin.readline으로 변경 후 제출해야 됨 (아니면 시간 초과)

[핵심 아이디어]
    1. 대기줄을 큐(deque)로 구현하여 선입선출 구조를 만든다
    2. 학생 도착(유형 1)과 식사 준비(유형 2)를 순서대로 시뮬레이션한다
    3. 식사할 때 선호 메뉴와 제공 메뉴를 비교하여 해당 리스트에 분류한다
    4. 모든 처리 후 큐에 남은 학생들은 식사를 못한 학생들이다

[풀이 과정]
    1. 큐와 세 개의 결과 리스트(A, B, C)를 초기화한다
    2. n개의 정보를 순서대로 처리한다
       - 유형 1: (학생번호, 선호메뉴)를 큐 뒤에 추가
       - 유형 2: 큐 앞에서 학생을 꺼내어 선호메뉴와 제공메뉴 비교 후 분류
    3. 처리 완료 후 큐에 남은 학생들을 C 리스트에 추가
    4. 각 리스트를 오름차순 정렬하여 출력 (빈 리스트는 "None" 출력)
"""

from collections import deque

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 6
# n_list = [
#     [1, 2, 1], [1, 1, 1], [2, 1], [1, 3, 2], [2, 2], [2, 2]
# ] # 2 3  \  1  \  None

queue = deque()  # 대기줄: (학생번호, 선호메뉴)
A = []  # 좋아하는 메뉴를 먹은 학생들
B = []  # 좋아하지 않는 메뉴를 먹은 학생들
C = []  # 식사를 못한 학생들

for info in n_list:
    if info[0] == 1:  # 유형 1: 학생 도착
        student_num, favorite_menu = info[1], info[2]
        queue.append((student_num, favorite_menu))

    elif info[0] == 2:  # 유형 2: 식사 준비
        served_menu = info[1]
        student_num, favorite_menu = queue.popleft()

        if favorite_menu == served_menu:
            A.append(student_num)  # 좋아하는 메뉴
        else:
            B.append(student_num)  # 좋아하지 않는 메뉴

# 대기줄에 남은 학생들은 식사를 못함
while queue:
    student_num, _ = queue.popleft()
    C.append(student_num)

def print_result(lst):
    if lst:
        lst.sort()
        print(' '.join(map(str, lst)))
    else:
        print("None")

print_result(A)
print_result(B)
print_result(C)
