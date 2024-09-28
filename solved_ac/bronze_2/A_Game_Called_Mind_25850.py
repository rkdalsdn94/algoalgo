# 백준 - 브론즈2 - A Game Called Mind - 25850 - 구현, 정렬, 시뮬레이션 문제
'''
구현, 정렬, 시뮬레이션 문제

단순히 정렬을 이용해서 구현하면 되는 문제이다.

풀이 과정
 1. 입력받은 c를 정렬하여 sorted_c에 저장한다.
 2. sorted_c를 순회하며 c에 있는지 확인하고 있다면 해당 인덱스를 출력한다.
 3. 출력할 때는 chr(65 + j)를 사용하여 A, B, C, D, E로 출력한다.
'''

p = int(input())
c = [list(map(int, input().split())) for _ in range(p)]

# 테스트
# p = 2
# c = [[3, 10, 40, 50], [2, 20, 30]] # ABBAA
# p = 3
# c = [[4, 40, 51, 60, 70], [3, 12, 32, 42], [5, 20, 53, 80, 90, 95]] # BCBABACAACCC

sorted_c = []
for i in range(p):
    sorted_c.extend(c[i][1:])

sorted_c.sort()
for i in sorted_c:
    for j in range(p):
        if i in c[j]:
            print(chr(65 + j), end='')
            break
