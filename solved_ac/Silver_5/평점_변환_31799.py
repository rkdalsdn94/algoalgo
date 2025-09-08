# 백준 - 실버5 - 평점 변환 - 31799 - 구현, 문자열, 파싱 문제
"""
구현, 문자열, 파싱

[핵심 아이디어]
    1. 문자열을 올바르게 파싱하여 개별 평어로 분리 (A, B, C는 A0, B0, C0으로 해석)
    2. 주어진 변환 규칙에 따라 현재 평어와 이전 학기 평어를 고려하여 새로운 평어로 변환

[풀이 과정]
    1. 입력 문자열을 왼쪽부터 읽으면서 개별 평어로 파싱
       - 다음 문자가 +, -, 0이면 2글자 평어
       - 그렇지 않으면 1글자 평어 (A→A0, B→B0, C→C0)
    2. 각 학기마다 현재 평어와 이전 학기 평어를 확인하여 변환 규칙 적용
    3. 변환된 결과를 순서대로 출력
"""

n = int(input())
grade_string = input().strip()

# 테스트
# n = 12
# grade_string = "A+BC+C0C-B0B-B+A0AC+C-" # EBBBBDBPEPBB
# n = 3
# grade_string = "ABC" # EBB
# n = 4
# grade_string = "A+A0AA-" # EPPD

grades = []
i = 0
while i < len(grade_string):
    if i + 1 < len(grade_string) and grade_string[i+1] in ['+', '-', '0']:
        # 2글자 (A+, A-, A0 등)
        grades.append(grade_string[i:i+2])
        i += 2
    else:
        # 1글자 (A, B, C를 A0, B0, C0으로 변환)
        grades.append(grade_string[i] + '0')
        i += 1

res = []
for i in range(n):
    current = grades[i]
    previous = grades[i-1] if i > 0 else None

    if current in ['C+', 'C0', 'C-']:
        # C+, C0, C- -> B
        res.append('B')
    elif current in ['B0', 'B-']:
        # B0, B- 변환 규칙
        if previous is None or previous in ['C+', 'C0', 'C-']:
            res.append('D')
        else:  # previous in ['A+', 'A0', 'A-', 'B+', 'B0', 'B-']
            res.append('B')
    elif current in ['A-', 'B+']:
        # A-, B+ 변환 규칙
        if previous is None or previous in ['B0', 'B-', 'C+', 'C0', 'C-']:
            res.append('P')
        else:  # previous in ['A+', 'A0', 'A-', 'B+']
            res.append('D')
    elif current == 'A0':
        # A0 변환 규칙
        if previous is None or previous in ['A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']:
            res.append('E')
        else:  # previous in ['A+', 'A0']
            res.append('P')
    elif current == 'A+':
        # A+ -> E (항상)
        res.append('E')

print(''.join(res))
