'''
처음에 kin이 어떻게 연속으로 나온다는 거지..?라고 하면서 문제를 이해 못하다가
이해한 순간 생가나는 대로 구현을 했다.
다른 사람 풀이에 보면 문자열 내장함수 중 count하는 사람도 있었는데, 그 방식도 괜찮은거 같다.
word를 한 글자씩 반복하면서 리스트에서 한 글자가 담겨져 있는지 && 리스트의 마지막과 word의 글자 이런 식으로 푸는것도 괜찮아 보인다.

in
    3
    happy
    new
    year
out
    3
in
    4
    aba
    abab
    abcabc
    a
out
    1
'''

n = int(input())
res = 0

for _ in range(n):
    flag = True
    word = input()

    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            pass
        elif word[i-1] in word[i:]:
            flag = False
            break
    
    if flag:
        res += 1

print(res)
