# 백준 - 실버5 - 날짜 계산 - 1476 - 수학, 정수론, 완전 탐색 문제
'''
수학, 정수론, 완전 탐색 문제

E : 지구를 나타내는 수 (1 <= 15)
S : 태양을 나타내는 수 (1 <= 28)
M : 달을 나타내는 수 (1 <= 19)

처음에 나이브하게 완전 탐색 방식으로 res와 a, b, c라는 변수를 만들고
1씩 더해가며 e, s, m 과 같을 때 res를 출력하는 방식으로 풀었다가 시간 초과가 나왔다.

그래서 다른 사람들의 풀이를 참고하니 res에 e, s, m 를 뺀 후, 최댓값으로 올 수 있는 수를 나머지 연산으로 0이 될 때 출력하는 방식을 사용하길래
해당 방식으로 제출했더니 통과했다. 마냥 완전 탐색으로 풀면 안 되는 문제다.

나머지 연산으로 문제를 풀고 난 후, '어떻게 양수로 음수를 나머지 연산이 가능하지?' 에 대해 의문이 생겨서 아래 링크를 통해 공부했다.
https://www.youtube.com/watch?v=qoZDaLe5_KE 음수 나머지에 대한 초등수학 설명

초등 수학을 생각해보면 단순한 문제였는데 초등 수학이 기억이 안나.. 조금 고생한 문제였다.
'''

e, s, m = map(int, input().split())

# 테스트
# e, s, m = 1, 16, 16 # 16
# e, s, m = 1, 1, 1 # 1
# e, s, m = 1, 2, 3 # 5266
# e, s, m = 15, 28, 19 # 7980

res = 1

while 1:
    if (res - e) % 15 == 0 and (res - s) % 28 == 0 and (res - m) % 19 == 0:
        print(res)
        break
    res += 1

'''
처음 코드 (시간 초과)

res, a, b, c = 0, 0, 0, 0

while 1:
    if [a,b,c] == [e,s,m]:
        print(res)
        break

    res += 1; a += 1; b += 1; c += 1
    if a >= 15:
        a = 0
    elif b >= 28:
        b = 0
    elif c >= 19:
        c = 0
'''