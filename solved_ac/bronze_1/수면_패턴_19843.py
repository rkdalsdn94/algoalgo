# 백준 - 브론즈1 - 수면 패턴 - 19843 - 단순 구현 문제
'''
단순 구현 문제

만약 67 % 에서 '틀렸습니다.'가 나온다면 시간을 구하는 부분에서 날짜가 2일 이상 바뀔수도 있다는 걸 생각해야 된다.
즉, 월요일 10시부터 자서 목요일 10시까지 잔다고 하면 72시간을 자는 것이다.
이 부분만 조심하고 풀면 된다.

풀이 과정
 - 입력을 받고, 날짜를 리스트에 저장한다.
 - 날짜를 리스트 값을 꺼내서 다음을 계산한다.
    - 날짜가 같으면 시간을 더하고, 날짜가 다르면 d2의 날짜를 달라진 요일 만큼 24를 더해야 된다. (24 * (day_list.index(d2) - day_list.index(d1)))
 - 위 반복문에서 평일의 수면 시간인 sleep_time 을 구한 뒤 이 값을 기준으로 t 랑 비교한다.
    - sleep_time 의 값이 t보다 크거나 같으면 0을 출력한다.
    - sleep_time 에 48을 더해도 t 보다 작다면 -1을 출력한다.
    - 나머지는 t에서 sleep_time의 값을 빼면 된다.
'''

t, n = map(int, input().split())
n_list = [list(input().split()) for _ in range(n)]

# 테스트
# t, n = 56, 6
# n_list = [
#     list('Mon 22 Tue 2'.split()),
#     list('Tue 15 Tue 19'.split()),
#     list('Tue 19 Wed 4'.split()),
#     list('Wed 17 Thu 1'.split()),
#     list('Thu 12 Thu 17'.split()),
#     list('Fri 4 Fri 12'.split())
# ] # 18
# t, n = 50, 5
# n_list = [
#     list('Mon 0 Mon 11'.split()),
#     list('Tue 2 Tue 12'.split()),
#     list('Tue 0 Wed 10'.split()),
#     list('Thu 3 Thu 15'.split()),
#     list('Fri 11 Fri 23'.split())
# ] # 0
# t, n = 120, 5
# n_list = [
#     list('Mon 0 Mon 11'.split()),
#     list('Tue 2 Tue 12'.split()),
#     list('Wed 0 Wed 10'.split()),
#     list('Thu 3 Thu 15'.split()),
#     list('Fri 11 Fri 23'.split())
# ] # -1

res = 0
sleep_time = 0
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

for d1, h1, d2, h2 in n_list:
    h1, h2 = int(h1), int(h2)

    if d1 == d2:
        sleep_time += h2 - h1
    elif day_list.index(d2) > day_list.index(d1):
        h2 += 24 * (day_list.index(d2) - day_list.index(d1))
        sleep_time += h2 - h1

if sleep_time >= t:
    print(0)
elif sleep_time + 48 < t:
    print(-1)
else:
    print(abs(t - sleep_time))
