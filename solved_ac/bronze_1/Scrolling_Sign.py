# 백준 - 브론즈1 - Scrolling Sign - 4187 - 구현, 문자열 문제
"""
구현, 문자열 문제

[핵심 아이디어]
    연속된 두 단어 사이의 최대 오버랩을 찾아서 재사용할 수 있는 문자 수를 계산합니다.
    현재 단어의 끝 i글자와 다음 단어의 앞 i글자가 일치하면, k-i개의 문자만 추가하면 됩니다.

[풀이 과정]
    1. 첫 번째 단어는 k개의 문자를 모두 입력 (초기 상태)
    2. 이후 각 단어마다 다음을 수행
       - 이전 단어의 마지막 부분과 현재 단어의 앞부분의 최대 오버랩 계산
       - 오버랩 길이가 i라면, k-i개의 문자만 추가
    3. 모든 필요한 문자 수를 합산

in
    2
    3 2
    CAT
    TED
    3 3
    CAT
    ATE
    TEA
out
    5
    5
"""

n = int(input())

for _ in range(n):
    k, w = map(int, input().split())
    words = [input().strip() for _ in range(w)]

    # 첫 번째 단어는 k개의 문자를 모두 입력해야 함
    total_chars = k

    # 두 번째 단어부터 처리
    for i in range(1, w):
        prev_word = words[i - 1]
        curr_word = words[i]

        # 최대 오버랩 찾기
        max_overlap = 0
        for overlap_len in range(1, k + 1):
            # 이전 단어의 마지막 overlap_len개 문자와
            # 현재 단어의 첫 overlap_len개 문자를 비교
            if prev_word[k - overlap_len:] == curr_word[:overlap_len]:
                max_overlap = overlap_len

        # 오버랩된 만큼 제외하고 나머지 문자만 추가
        total_chars += k - max_overlap

    print(total_chars)
