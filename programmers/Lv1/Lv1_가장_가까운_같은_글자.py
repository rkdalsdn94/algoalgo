# 프로그래머스 - Lv1 - 가장 가까운 같은 글자 - 문자열, 해시(딕셔너리) 문제
'''
문자열, 해시(딕셔너리) 문제

[핵심 아이디어]
    각 문자의 가장 최근 등장 위치를 딕셔너리에 저장하여, 현재 위치와의 차이를 계산한다.
    이를 통해 O(n) 시간 복잡도로 문제를 해결할 수 있다.

[풀이 과정]
    1. 결과를 저장할 리스트 answer를 초기화한다.
    2. 각 문자의 가장 최근 등장 위치를 저장할 딕셔너리 last_position을 초기화한다.
    3. 문자열 s를 순회하면서 각 문자를 처리한다:
       - 문자가 이미 last_position에 존재하는 경우:
         - 현재 위치(i)와 해당 문자의 마지막 등장 위치의 차이를 계산하여 answer에 추가한다.
       - 문자가 last_position에 존재하지 않는 경우:
         - -1을 answer에 추가한다.
       - 현재 문자의 위치 정보를 last_position에 업데이트한다.
    4. 모든 문자 처리가 끝나면 answer를 반환한다.
'''

def solution(s):
    answer = []
    last_position = {}  # 각 문자의 마지막 등장 위치를 저장하는 딕셔너리

    for i in range(len(s)):
        if s[i] in last_position:
            # 현재 위치와 마지막 등장 위치의 차이를 계산
            answer.append(i - last_position[s[i]])
        else:
            # 처음 등장한 문자인 경우
            answer.append(-1)

        # 현재 문자의 위치 정보 업데이트
        last_position[s[i]] = i

    return answer

print(solution("banana") == [-1, -1, -1, 2, 2, 2])
print(solution("foobar") == [-1, -1, 1, -1, -1, -1])
