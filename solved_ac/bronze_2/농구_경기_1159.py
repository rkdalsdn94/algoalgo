'''
구현, 문자열 문제

단순 문자열 구현 문제이다.
근데, 반환할 때 ''.join 을 하지 않고, sorted를 하지 않았을 때
틀렸습니다가 나온다...? 이건 이유를 잘 모르겠다..

적혀진 대로 5이상을 찾고 (set으로 한 이유는 반복문 수를 줄이고, res에 중복값 제거를 위해서)
값이 있으면 res 출력 없으면 'PREDAJA' 출력한다.
'''

n = int(input())
plays = [ input()[0] for _ in range(n) ]

# 테스트
# n = 18
# plays = sorted(['b', 'k', 'b', 'b', 's', 'b', 'k', 'h', 'b', 'b', 'k', 'p', 'k', 'k', 's', 'k', 'k', 'p']) # bk
# n = 6
# plays = sorted(['m', 'j', 'l', 'j', 'k', 'b']) # PREDAJA

res = ''

for i in set(plays):
    if plays.count(i) >= 5:
        res += (i)

print( ''.join(sorted(res)) if res else 'PREDAJA' )
