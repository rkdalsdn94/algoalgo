# 백준 - 골드4 - 전화번호 목록 - 5052 - 문자열, 정렬 문제
'''
문자열, 정렬 문제

- 풀이 과정 -
1. 문자열을 리스트로 입력 받는다.
    ㄴ> 1.1 res는 'YES'로 초기화한다, 
    ㄴ> 1.2 입력받은 문자열 리스트에 처음 값을 temp에 저장한다.
2. 입력받은 문자열 리스트에서 처음을 제외한 나머지 길이 만큼 반복한다(n - 1의 길이 만큼)
    ㄴ> 2.1 temp에 저장된 값으로 파이썬에서 문자열 내장 함수로 있는 startswith 함수를 통해 검사한다.
    ㄴ> 2.2 startswith 함수가 해당 글자가 현재 글자의 시작 부분이랑 동일하면 True, False를 반환한다.
    ㄴ> 2.3 True이면 res를 'NO'로 바꾸고 반복문을 종료한다.
    ㄴ> 2.4 False이면 temp를 현재 반복중인 문자열로 바꿔준 후에 2.1로 돌아간다.
3. res를 출력한다.

느낀점..
이 문제에선 rstrip을 안하면 틀렸다고 나온다. 아마 입력 문자중 끝에 공백값이 들어오는 경우도 있는거 같다.
처음에는 startswith 함수를 모르고 아래쪽에 코드로 통과했다가 다른 사람 코드에서 저 함수가 더 깔끔한거 같아 변경했다.
나중에는 Trie 자료 구조로 시도해보면 좋을거 같다.

in
    2
    3
    911
    97625999
    91125426
    5
    113
    12340
    123440
    12345
    98346
out
    NO
    YES
'''
import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    word = sorted([ input().rstrip() for _ in range(n) ])
    res = 'YES'
    temp = word[0]

    for i in range(1, n):
        if word[i].startswith(temp):
            res = 'NO'
            break
        temp = word[i]

    print(res)


############################
'''
# 처음 코드이다.
for _ in range(t):
    n = int(input())
    word = sorted([ input().rstrip() for _ in range(n) ])
    res = 'YES'
    temp = word[0]

    for i in range(1, n):
        if temp == word[i][:len(temp)]:
            res = 'NO'
            break
        temp = word[i]

    print(res)
'''