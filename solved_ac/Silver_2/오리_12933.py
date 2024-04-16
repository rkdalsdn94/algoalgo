# 백준 - 실버2 - 오리 - 12933 - 구현, 문자열, 그리디 문제
'''
구현, 문자열, 그리디 문제

만약 64% 쯤에서 틀린다면 시작 글자가 'q' 인지, 끝 글자가 'k'인지, 길이가 5의 배수인지 확인해야 한다.

풀이 과정
1. 입력을 받고, 'quack'의 순서대로 문자열을 찾아야 한다.
2. 'quack'의 순서대로 찾아야 하므로, 'q'를 찾고, 'u'를 찾고, 'a'를 찾고, 'c'를 찾고, 'k'를 찾는다.
3. 'k'를 찾으면, 'quack'을 찾은 것이므로, res를 1 증가시키고, 다시 'q'를 찾는다.
    3.1. 이때 flag를 사용해서, 'quack'을 찾았을 때, res를 1 증가시키고, flag를 False로 바꾼다. 이유는, 한 마리의 오리가 연속으로 우는 것이기 때문이다.
4. 만약, 'quack'을 찾지 못하면, -1을 출력한다.
5. 첫 글자와 마지막 글자, 길이가 5의 배수인지 확인한다.
'''

word = input()

# 테스트
# word = 'quqacukqauackck' # 2
# word = 'kcauq' # -1
# word = 'quackquackquackquackquackquackquackquackquackquack' # 1
# word = 'qqqqqqqqqquuuuuuuuuuaaaaaaaaaacccccccccckkkkkkkkkk' # 10
# word = 'quqaquuacakcqckkuaquckqauckack' # 3
# word = 'quackqauckquack' # -1

ck = [0] * len(word)
duck = 'quack'
res = 0

if word[0] != 'q' or word[-1] != 'k' or len(word) % 5 != 0: # 64% 쯤에서 틀렸을 때 예외 처리
    print(-1)
    exit()

for i in range(len(word)):
    flag = True
    idx = 0

    for j in range(i, len(word)):
        if word[j] == duck[idx] and ck[j] == 0:
            ck[j] = 1

            if word[j] == 'k' and idx == 4:
                if flag:
                    res += 1
                    flag = False
                idx = 0
                ck[j] = 1

            elif word[j] == duck[idx]:
                ck[j] = 1
                idx += 1

    if 0 not in ck:
        break

print(res if 0 not in ck else -1)


'''
처음 틀린 풀이 (중간의 반복문 부분과 flag를 사용하지 않은 부분이 문제)

for i in range(len(word)):
    if word[i] == 'q' and ck[i] == 0:
        ck[i] = 1

        for j in range(i + 1, len(word)):
            if word[j] == 'k' and idx == 4: # 연속된 오리를 체크하지 못 한다.
                res += 1
                idx = 1
                break

            if ck[j] == 0 and word[j] == duck[idx]:
                ck[j] = 1
                idx += 1
'''
