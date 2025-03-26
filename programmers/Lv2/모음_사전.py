# 프로그래머스 - Lv2 - 모음 사전 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    1. 각 자리수마다 가중치를 계산하여 단어의 순서를 결정한다
    2. 뒤에서부터 앞으로 탐색하며 각 자리의 알파벳에 따른 순서를 계산한다
    3. 각 자리의 알파벳이 사전상 몇 번째인지에 따라 그 뒤에 올 수 있는 모든 경우의 수를 더한다


[풀이 과정]
    1. 각 자리에서 한 글자가 바뀔 때마다 뒤에 올 수 있는 모든 경우의 수를 계산한다
    2. 이를 위해 각 자리수별로 5의 거듭제곱 값을 미리 계산해둔다
    3. 단어의 마지막 글자부터 첫 글자까지 역순으로 탐색하며:
       - 현재 글자의 사전상 위치(인덱스)를 찾는다
       - 해당 위치에 따라 그 뒤에 올 수 있는 모든 경우의 수를 더한다
       - 각 글자마다 기본 1을 더해 해당 글자 자체의 위치를 계산한다
"""

def solution(word):
    answer = 0
    word_list = ['A', 'E', 'I', 'O', 'U']
    temp = [5 ** i for i in range(len(word_list))]

    for i in range(len(word) - 1, -1, -1):
        idx = word_list.index(word[i])

        for j in range(5 - i):
            answer += temp[j] * idx
        answer += 1

    return answer

print(solution("AAAAE") == 6)
print(solution("AAAE") == 10)
print(solution("I") == 1563)
print(solution("EIO") == 1189)
