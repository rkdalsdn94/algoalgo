# 프로그래머스 - Lv2 - 압축 - 문자열, 자료구조(해시), 구현 문제
"""
문자열, 자료구조(해시), 구현 문제

[핵심 아이디어]
    1. LZW 압축 알고리즘을 구현하기 위해 현재 처리 중인 문자열(w)과 다음 문자(c)를 관리
    2. 해시맵(딕셔너리)을 이용해 문자열과 색인 번호 간의 매핑을 저장
    3. 탐욕적 접근 방식으로 사전에서 가장 긴 일치하는 문자열을 찾음
    4. 사전에 없는 문자열을 만났을 때 색인 번호를 출력하고 새 문자열을 사전에 추가

[풀이 과정]
    1. 영문 대문자(A-Z)로 사전을 초기화 (색인 번호 1-26)
    2. 현재 위치(current)와 다음 위치(next)를 통해 문자열을 탐색
    3. 문자열을 순회하면서:
       a. 다음 위치를 한 칸 이동
       b. 현재 위치부터 다음 위치까지의 문자열이 사전에 없으면:
          - 해당 문자열을 사전에 추가 (색인 번호는 사전 크기 + 1)
          - 이전 문자열의 색인 번호를 결과에 추가
          - 현재 위치를 다음 위치로 이동
       c. 사전에 있으면 계속 탐색 진행
    4. 마지막 문자열의 색인 번호를 결과에 추가
"""

def solution(msg):
    answer = []
    word_dic = {chr(i + 64): i for i in range(1, 27)}
    cur_idx, next_idx = 0, 0

    while 1:
        next_idx += 1
        if next_idx == len(msg):
            answer.append(word_dic[msg[cur_idx:next_idx]])
            break

        if msg[cur_idx:next_idx + 1] not in word_dic:
            word_dic[msg[cur_idx:next_idx + 1]] = len(word_dic) + 1
            answer.append(word_dic[msg[cur_idx:next_idx]])
            cur_idx = next_idx

    return answer

print(solution('KAKAO') == [11, 1, 27, 15])
res = [
    20, 15, 2, 5, 15,
    18, 14, 15, 20, 27,
    29, 31, 36, 30, 32, 34
]
print(solution('TOBEORNOTTOBEORTOBEORNOT') == res)
res = [
    1, 2, 27, 29, 28, 31, 30
]
print(solution('ABABABABABABABAB') == res)
