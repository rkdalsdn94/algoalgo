# 백준 - 실버4 - 카드셋트 - 11507 - 자료 구조(해시), 문자열, 파싱 문제
'''
자료 구조(해시), 문자열, 파싱 문제

풀이 과정
    1. 입력을 받는다.
    2. res를 딕셔너리(해시)로 만들어 3글자 씩 쪼갠 값을 저장한다.
    3. res 딕셔너리의 키의 길이가 word의 길이 // 3보다 작다면 2개의 같은 카트가 존재하는 것이므로 GRESKA를 출력한다.
    4. word 길이 // 3 보다 크면 다음의 과정을 실행한다.
        4.1. p, k, h, t를 13으로 초기화한다.
        4.2. res의 key를 돌면서 각각의 카드의 값을 1씩 빼준다. (p, k, h, t) 값을 1씩 빼주기
        4.3. p, k, h, t의 값을 출력한다.
'''

word = input()

# 테스트
# word = 'P01K02H03H04' # 12 12 11 13
# word = 'H02H10P11H02' # GRESKA
# word = 'P10K10H10T01' # 12 12 12 12

res = {}
for i in range(0, len(word), 3):
    temp = word[i:i + 3]

    if temp[0] in res:
        res[temp] += 1
    else:
        res[temp] = 1

if len(res.keys()) < len(word) // 3:
    print('GRESKA')
else:
    p, k, h, t = 13, 13, 13, 13

    for i in res.keys():
        if i[0] == 'P':
            p -= 1
        elif i[0] == 'K':
            k -= 1
        elif i[0] == 'H':
            h -= 1
        else:
            t -= 1

    print(p, k, h, t)
