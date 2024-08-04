# 백준 - 실버2 - DNA 비밀번호 - 12891 - 문자열, 슬라이딩 윈도우 문제
'''
문자열, 슬라이딩 윈도우 문제

슬라이딩 윈도우 방식으로 문제를 풀 수 있다.
리스트로 풀었는데.. 다른 사람의 풀이를 보면 딕셔너리를 사용하는 게 훨씬 깔끔하다.
적절한 자료 구조를 잘 활용하자.

풀이 과정
    1. 입력을 받는다.
    2. temp에 A, C, G, T의 개수를 저장한다.
    3. left, right를 0, p-1로 초기화한다.
    4. res를 0으로 초기화한다.
    5. right가 s보다 작을 때까지 반복한다.
        5.1. right가 가리키는 문자를 temp에 저장한다.
        5.2. temp의 값이 dna의 값보다 크거나 같으면 res에 1을 더한다.
        5.3. left가 가리키는 문자를 temp에서 빼준다.
        5.4. left, right를 1씩 증가시킨다.
    6. res를 출력한다.
'''

s, p = map(int, input().split())
word = input()
dna = list(map(int, input().split()))

# 테스트
# s, p = 9, 8
# word = 'CCCTGGATTG'
# dna = [2, 0, 1, 1,] # 0
# s, p = 4, 2
# word = 'GATA'
# dna = [1, 0, 0, 1] # 2

temp = [0, 0, 0, 0]
left, right = 0, p - 1
res = 0

for i in range(p - 1):
    if word[i] == 'A':
        temp[0] += 1
    elif word[i] == 'C':
        temp[1] += 1
    elif word[i] == 'G':
        temp[2] += 1
    elif word[i] == 'T':
        temp[3] += 1

while right < s:
    if word[right] == 'A':
        temp[0] += 1
    elif word[right] == 'C':
        temp[1] += 1
    elif word[right] == 'G':
        temp[2] += 1
    elif word[right] == 'T':
        temp[3] += 1

    if temp[0] >= dna[0] and temp[1] >= dna[1] and temp[2] >= dna[2] and temp[3] >= dna[3]:
        res += 1

    if word[left] == 'A':
        temp[0] -= 1
    elif word[left] == 'C':
        temp[1] -= 1
    elif word[left] == 'G':
        temp[2] -= 1
    elif word[left] == 'T':
        temp[3] -= 1

    left += 1
    right += 1

print(res)

'''
딕셔너리를 활용한 풀이

N, M = map(int, input().split())
DNA = input().strip()
S = list(map(int, input().split()))

ans = 0
cnt = [0, 0, 0, 0]
dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(M):
    cnt[dic[DNA[i]]] += 1

for k in range(4):
    if cnt[k] < S[k]:
        break
else:
    ans += 1

for i in range(N - M):
    cnt[dic[DNA[i]]] -= 1
    cnt[dic[DNA[i+M]]] += 1

    for k in range(4):
        if cnt[k] < S[k]:
            break
    else:
        ans += 1

print(ans)
'''
