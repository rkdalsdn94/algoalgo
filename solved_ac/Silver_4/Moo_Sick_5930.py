# 백준 - 실버4 - Moo Sick - 5930 - 구현, 완전 탐색, 정렬 문제
"""
구현, 완전 탐색, 정렬 문제

[핵심 아이디어]
    1. 화음의 전조(transposition)와 재배열(re-ordering)을 처리하기 위해 정규화 사용
    2. 정규화: 음표들을 정렬한 후 최소값을 0으로 만들어 상대적 간격만 유지
    3. 노래에서 연속된 C개 음표씩 슬라이딩 윈도우로 확인하여 패턴 매칭

[풀이 과정]
    1. 주어진 ruminant seventh chord를 정규화하여 기준 패턴 생성
    2. 노래에서 연속된 C개 음표마다:
       a. 해당 구간을 같은 방식으로 정규화
       b. 기준 패턴과 비교하여 일치하면 시작 인덱스 저장
    3. 찾은 모든 시작 인덱스를 정렬하여 출력
"""

n = int(input())
song = [int(input()) for _ in range(n)]
c = int(input())
chord = [int(input()) for _ in range(c)]

# 테스트
# n = 6
# song = [1, 8, 5, 7, 9, 10]
# c = 3
# chord = [4, 6, 7] # 2  \  2  \  4

def normalize_chord(notes):
    """화음을 정규화하는 함수: 정렬 후 최소값을 0으로 만듦"""
    sorted_notes = sorted(notes)
    min_note = min(sorted_notes)
    return [note - min_note for note in sorted_notes]

target_pattern = normalize_chord(chord)
res = []

# 슬라이딩 윈도우로 노래의 연속된 C개 음표 확인
for i in range(n - c + 1):
    # 현재 위치에서 C개 음표 추출
    current_segment = song[i:i+c]

    # 현재 구간 정규화
    current_pattern = normalize_chord(current_segment)

    # 기준 패턴과 비교
    if current_pattern == target_pattern:
        res.append(i + 1)  # 1-based 인덱스

print(len(res))
for index in res:
    print(index)
