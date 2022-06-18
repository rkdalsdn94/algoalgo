'''
단순 구현 문제

단순하게 구현하기만 하면 되는데
처음 시작을 1 + 2 인 상태 -> 3으로 시작해야 되는거만 주의하면 된다.
그리고 입력받은 word의 한 글자씩 돌면서 dic으로 만든 값이 있으면
res에 더해주고 글자를 다 돌면 더해진 res를 출력하면 된다.
'''

word = input()

# 테스트
# word = 'WA' # 13
# word = 'UNUCIC' # 36

dic = {
    3: 'ABC', 4: 'DEF', 5: 'GHI', 6: 'JKL',
    7: 'MNO', 8: 'PQRS', 9: 'TUV', 10: 'WXYZ',
    11: 'OPERATOR'
}
res = 0

for i in range(len(word)):
    for k, v in dic.items():
        if word[i] in v:
            res += k
            break

print(res)
