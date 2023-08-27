# 백준 - 골드4 - 문자열 폭발 - 9935 - 자료 구조(스택), 문자열 문제
'''
자료 구조(스택), 문자열 문제

리스트(res, 파이선에선 리스트가 스택)에 word의 값을 append 한다.
한 글자씩 res 에 append 할 때 마다 target 의 길이로 뒤에서 리스트 슬라이싱을 했을 때의 값이 target 이랑 같으면 해당 글자를 리스트(res)에서 뺀다.

word 의 길이로 위 같은 과정을 반복한 다음 res에 값이 있다면 있다면 그 값을 출력하면 되고, 없다면 'FRULA'를 출력하면 된다.
'''

word = input()
target = list(input())

# 테스트
# word = 'mirkovC4nizCC44'
# target = 'C4' # mirkovniz
# word = '12ab1112ab2ab'
# target = '12ab' # FRULA

res = []
for i in range(len(word)):
    res.append(word[i])
    if res[-len(target):] == target:
        for _ in range(len(target)):
            res.pop()

if res:
    print(''.join(res))
else:
    print('FRULA')
