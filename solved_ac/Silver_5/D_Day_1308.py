# 백준 - 실버5 - D Day - 1308 - 구현 문제
'''
구현 문제

처음에 풀 때는 단순하게 모두 몇 개의 일(날짜)로 바꿔 구현했다. 이렇게 풀면 코드의 양도 많아지고, 복잡도도 높아진다.
그러다 다른 사람의 코드르 보니 date를 모듈을 사용하길래 이 방식이 더 간단하고, 효율적이라 다시 풀었다.

풀이 과정
    1. 오늘 날짜와 D-Day 날짜를 입력받는다.
    2. 만약 d-day가 오늘 날짜(today)의 천년 뒤에 있다면 'gg'를 출력한다.
    3. 또한, d-day가 오늘 날짜(today)의 천년 뒤에 있고, 오늘 날짜(today)가 D-Day 날짜보다 작거나 같다면 'gg'를 출력한다.
    4. 위 조건들에서 걸러지지 않는다면 date를 사용해 오늘 날짜와 D-Day 날짜를 만든다.
    5. res를 만들어 D-Day 날짜 - 오늘 날짜를 구해 출력한다.
'''

from datetime import date

today = list(map(int, input().split()))
d_day = list(map(int, input().split()))

# 테스트
# today = list(map(int, '2008 12 27'.split()))
# d_day = list(map(int, '2009 1 22'.split())) # D-26
# today = list(map(int, '2008 12 27'.split()))
# d_day = list(map(int, '3009 1 22'.split())) # gg

if today[0] + 1000 < d_day[0]:
    print('gg')
elif today[0] + 1000 == d_day[0] and today[1:] <= d_day[1:]:
    print('gg')
else:
    today = date(today[0], today[1], today[2])
    d_day = date(d_day[0], d_day[1], d_day[2])
    res = d_day - today
    print(f'D-{res.days}')
