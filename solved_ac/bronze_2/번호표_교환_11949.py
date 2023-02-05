# 백준 - 브론즈2 - 번호표 교환 - 11949 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

아래 조건을 구하면 되는 문제이다.
 - 선생님이 1번 학생에게 i번 카드를 준다. (1 ≤ i ≤ M)
 - 카드를 받은 j번 학생은 j+1번 학생에게 카드를 넘긴다.
 - Aj % i의 값이 Aj+1%i 의 값보다 크면 두 학생의 번호표를 서로 교환한다.
 - 마지막 학생이 카드를 받으면 그 카드는 버린다.
'''

n, m = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n, m = 6, 4
# n_list = [ 3, 2, 8, 3, 1, 5 ] # 2  \  3  \  1  \  8  \  5  \  3
# n, m = 10, 6
# n_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] # 6  \  1  \  2  \  3  \  10  \  4  \  8  \  7  \  9  \  5

for i in range(1, m + 1):
    for j in range(1, len(n_list)):
        if n_list[j - 1] % i > n_list[j] % i:
            n_list[j - 1], n_list[j] = n_list[j], n_list[j - 1]

for i in n_list:
    print(i)
