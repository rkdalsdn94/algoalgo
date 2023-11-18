# 백준 - 브론즈1 - 이번학기 평점은 몇점 - 2755 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

(백준 - solved.ac - 18110) 이 문제에서 봤듯이 '오사오입' 때문에 문제가 발생한다.
이 부분만 잘 해결하고 구현하면 되는 어렵지 않은 문제이다.
이 부분에 대한 해결을 이번에는 10**-10을 더하고(엄청 작은 수의 소수점을 더한 뒤
round 함수의 2번째 인자인 반올림할 자릿수를 2로 지정했다.
'%.2f'는 혹시 '3.0' 이런 식으로 0으로 떨어질 경우 '3.00'으로 맞추기 위해 했다.

in
    7
    General_Physics_1 3 A+
    Introduction_to_Computer_Science_and_Eng 3 B0
    Reading_And_Writing 2 C0
    English_1 3 C+
    Analytic_Geometry_and_Calculus_1 3 B+
    Fortran_Programming 3 B+
    C_Language_Programming 3 A+
out
    3.28
'''

n = int(input())

score_dic = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}
total_grade = 0
credit = 0

for _ in range(n):
    a, b, c = input().split()
    total_grade += score_dic[c] * int(b)
    credit += int(b)

print('%.2f' % (round(total_grade/credit + 0.0000000000001, 2)))
