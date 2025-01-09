# 백준 - 실버4 - Missing Vowels - 30608 - 그리디, 문자열 문제
'''
그리디, 문자열 문제

70% 정도에서 '틀렸습니다.' 가 나오면 다음의 상황을 고려해야 된다.
짧은 문자열을 긴 문자열을 통해 모두 완성할 수 있지만, 긴 문자열의 나머지 문자들이 모음에 속하지 않으면 'Different'를 출력해야 됨
예제를 통해 확인해보자.
in
    abc
    abcdef (짧은 문자열을 다 채우고, 긴 문자열에 나머지 글자가 모음에 속하지 않은 경우)
out
    Different

핵심 아이디어
    - 짧은 문자열이 긴 문자열에서 모음을 제거하여 얻을 수 있는지 확인
    - 두 포인터를 사용하여 각 문자열을 순차적으로 비교
    - 긴 문자열에서 모음을 건너뛰며 짧은 문자열과 매칭
    - 남은 문자들이 모두 모음인지 확인하는 추가 검증 필요

풀이 과정
    1. 두 문자열을 소문자로 변환하여 대소문자 구분 제거
    2. 짧은 문자열과 긴 문자열의 각 위치를 추적하는 두 개의 포인터 사용
    3. 문자 비교 진행:
        - 문자가 일치하면 두 포인터 모두 이동
        - 긴 문자열의 현재 문자가 모음이면 해당 포인터만 이동
        - 불일치하고 모음도 아니면 매칭 실패
    4. 짧은 문자열의 모든 문자가 매칭되었는지 확인
    5. 긴 문자열의 남은 문자들이 모두 모음인지 검증
    6. 결과에 따라 "Same" 또는 "Different" 출력
'''

# 모음 집합
vowels = set('aeiouy')

def can_obtain_short_name(s, f):
    s_idx = 0  # 짧은 이름의 현재 위치
    f_idx = 0  # 긴 이름의 현재 위치

    while s_idx < len(s) and f_idx < len(f):
        if s[s_idx] == f[f_idx]:  # 문자가 일치하는 경우
            s_idx += 1
            f_idx += 1
        elif f[f_idx] in vowels:  # 긴 이름의 현재 문자가 모음인 경우
            f_idx += 1
        else:  # 문자가 일치하지 않고, 긴 이름의 문자가 모음이 아닌 경우
            return False

    # 짧은 이름의 모든 문자를 찾았는지 확인
    if s_idx == len(s):
        # 긴 이름의 남은 문자들이 모두 모음인지 확인
        while f_idx < len(f):
            if f[f_idx] not in vowels:
                return False
            f_idx += 1
        return True
    return False

s, f = input(), input()

# 테스트
# s, f = 'Shrm-el-Shikh', 'Sharm-el-Sheikh' # Same
# s, f = 'Eilot', 'Eilat' # Different
# s, f = 'Saint-Petersburg', 'Saint-Petersburg' # Same
# s, f = 'Bcdfghjklmnpqrstvwxz', 'Abcdefghijklmnopqrstuvwxzyy' # Same
# s, f = 'Aa', 'aaaA' # Same
# s, f = 'Etis-Atis-Amatis', 'Etis-Atis-Animatis' # Different
# s, f = 'will-the-wisp', 'will-o-the-wisp' # Different
# s, f = '--a-very-short-name--', 'long-name' # Different
# s, f = 'abc', 'abcdef' # Different # 70% 에서 틀릴 때 확인해 볼 예제

s, f = s.lower(), f.lower()
print('Same' if can_obtain_short_name(s, f) else 'Different')
