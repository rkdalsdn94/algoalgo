# 프로그래머스 - Lv1 - 데이터 분석 - 정렬 문제
"""
정렬 문제

[핵심 아이디어]
    1. 주어진 조건(ext)에 따라 데이터를 필터링한다.
    2. 필터링된 데이터를 지정된 기준(sort_by)에 따라 정렬한다.
    3. 인덱스 매핑을 활용하여 문자열 조건을 정수 인덱스로 변환한다.

[풀이 과정]
    1. 'code', 'date', 'maximum', 'remain'을 인덱스로 매핑하는 리스트를 생성한다.
    2. 문자열 형태의 ext와 sort_by를 인덱스 값으로 변환한다.
    3. 데이터를 순회하면서 ext 조건(data[i][ext] < val_ext)에 맞는 항목만 추출한다.
    4. 추출된 데이터를 sort_by 기준으로 정렬하여 반환한다.
"""

def solution(data, ext, val_ext, sort_by):
    answer = []
    sort_option = ['code', 'date', 'maximum', 'remain']
    sort_by = sort_option.index(sort_by)
    ext = sort_option.index(ext)

    for i in range(len(data)):
        if data[i][ext] < val_ext:
            answer.append(data[i])

    return sorted(answer, key=lambda x: x[sort_by])

res = [[3,20300401,10,8],[1,20300104,100,80]]
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
print(solution(data, ext, val_ext, sort_by) == res)
