# 프로그래머스 - Lv1 - 문자열 나누기 - 문자열, 구현 문제
'''
문자열, 구현 문제

[핵심 아이디어]
    기준 문자의 출현 횟수와 다른 문자들의 출현 횟수를 세어 두 횟수가 동일해지는 시점에 문자열을 분리하는 과정을 반복하는 문제

[풀이 과정]
    1. 처음 만나는 문자를 기준 문자(standard)로 설정합니다.
    2. 기준 문자가 나타나면 same_cnt를 증가시키고, 다른 문자가 나타나면 diff_cnt를 증가
    3. same_cnt와 diff_cnt가 같아지면 지금까지 읽은 부분을 하나의 문자열로 분리하고, answer 증가
    4. 남은 문자열에 대해 1-3 과정을 반복합니다.
    5. 모든 문자를 처리한 후에도 same_cnt + diff_cnt > 0이면(분리되지 않은 문자가 있으면) 마지막 부분을 하나의 문자열로 간주, answer 증가
'''

def solution(s):
    answer = 0
    same_cnt, diff_cnt = 0, 0
    standard, temp = '', ''  # standard: 기준 문자, temp: 현재 문자

    for i in range(len(s)):
        if same_cnt == 0:  # 새로운 문자열 시작
            standard = s[i]
            same_cnt += 1
            continue
        else:
            temp = s[i]

            if temp == standard:  # 기준 문자와 같으면
                same_cnt += 1
                continue
            diff_cnt += 1  # 기준 문자와 다르면

        if same_cnt == diff_cnt:  # 두 횟수가 같아지면 분리
            answer += 1
            same_cnt, diff_cnt = 0, 0
            continue

    if same_cnt + diff_cnt > 0:  # 남은 문자열이 있으면 하나의 문자열로 처리
        answer += 1

    return answer

print(solution("banana") == 3)  # ba - na - na
print(solution("abracadabra") == 6)  # ab - ra - ca - da - br - a
print(solution("aaabbaccccabba") == 3)  # aaabbacc - ccab - ba
