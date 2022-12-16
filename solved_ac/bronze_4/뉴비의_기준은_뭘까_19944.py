# 백준 - 19944 - 브론즈4 - 뉴비의 기준은 뭘까? - 단순 구현 문제
'''
단순 구현 문제

조건문만 사용해서 풀면 된다.

풀이 과정
1. 입력으로 들어온 두 수를 비교한 후 출력하면 된다.
    m이 2보다 작거나 같으면 NEWBIE!
    m이 2보다 크고 n보다 작거나 같으면 OLDBIE!
    나머지는 TLE 로 출력하면 된다.
'''

n, m = map(int, input().split())

# 테스트
# n, m = 3, 1 # NEWBIE!
# n, m = 3, 5 # TLE!
# n, m = 3, 3 # OLDBIE!

if m <= 2:
    print('NEWBIE!')
elif m > 2 and m <= n:
    print('OLDBIE!')
else:
    print('TLE!')