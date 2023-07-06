# 백준 - 실버5 - 너의 평점은 - 25206 - 수학, 구현, 문자열 문제
'''
수학, 구현, 문자열 문제

문제에 있는 아래 부분을 구하면 되는 문제이다.
'전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.'
20개의 과목명과 학점, 등급을 입력받은 후 등급이 P이면 무시한다.
P가 아닐때엔 전체 점수를 담기 위해 subject_sum_score에 점수와 해당 등급의 점수를 곱한 값으로 더해준다.
학점의 총합으로 나누기 위해 total_score 에 score 값을 더해준다.
출력할 때 소수점 6자리 까지만 조심하고 subject_sum_score를 total_score로 나눈 값을 출력하면 된다.
'''

grades = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}
subject_sum_score = 0
total_score = 0

for i in range(20):
    subject_name, score, grade = input().split()

    if grade == 'P':
        continue

    subject_sum_score += float(score) * grades[grade]
    total_score += float(score)
print('{:6f}'.format(subject_sum_score / total_score))
