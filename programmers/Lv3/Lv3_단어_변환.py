# 프로그래머스 - Lv3 - 단어 변환 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

bfs로 풀었다.
refactor: 처음 코드에는 예제 1을 통과하지 못 한다. (근데 왜 통과했지..?)
예제 1을 통과할 수 있도록 코드를 수정하고 다시 제출했다.

풀이 과정
 1. target이 words에 없으면 0을 반환한다.
 2. stack에 begin을 넣는다.
 3. stack이 빌 때까지 반복한다.
 4. stack에서 pop한 word가 target이면 answer를 반환한다.
 5. words를 순회하면서 ck가 0이면 temp를 0으로 초기화한다.
 6. word와 words[i]를 비교하면서 다른 부분이 1개면 temp를 1 증가시킨다.
 7. temp가 1이면 ck[i]를 1로 바꾸고 stack에 words[i]를 넣는다.
 8. answer를 1 증가시킨다.
 9. 4번으로 돌아가 반복한다.
'''

from collections import deque

def solution(begin, target, words):
    ck = [0] * len(words)
    stack = deque([[begin, 0]])

    if target not in words:
        return 0

    while stack:
        word, cnt = stack.popleft() # 이 문제에선 pop을 하던 popleft를 하던 상관 없다.

        if word == target:
            return cnt

        for i in range(len(words)):
            if ck[i] == 0:
                temp = 0

                for j in range(len(words[i])):
                    if word[j] != words[i][j]:
                        temp += 1

                if temp == 1:
                    ck[i] = 1
                    stack.append([words[i], cnt + 1])

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0
