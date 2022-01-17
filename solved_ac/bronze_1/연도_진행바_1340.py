
'''
calendar 딕셔너리에다 달의 이름을 잘못 넣어 틀리고,
윤년의 계산중 마지막 % 100 != 0 이 되어야 되는데 나머지 연산자가 아니라 실수로 곱하기를 해놔서 여러번 틀렸었다.
예제만 봤을때 다 통과 하길래 제출 후 왜 틀리는지 찾는데 시간이 좀 걸렸다.
반례를 찾는 연습을 좀 더 해야될거 같다. (조건 속에서 정상 동작 하는 느낌으로 이 문제에선 4로 나누어 떨어지고 100으론 나누어 떨어지지 않는 년도에 대해 생각해 봤었으면 좋았을거 같다.)
'''
month, day, year, time = input().split()
# 테스트
# month, day, year, time = ['May', '10,', '1981', '00:31'] # 35.348363774733635
# month, day, year, time = ['January', '01,', '2008', '00:00'] # 0.0
# month, day, year, time = ['December', '31,', '2007', '23:59'] # 99.99980974124807
# month, day, year, time = ['July', '02,', '2007', '12:00'] # 50.0
# month, day, year, time = ['July', '02,', '2008', '00:00'] # 50.0
# month, day, year, time = ['January', '31,', '1900', '00:47'] # 8.228120243531203
day, year, time = int(day[:-1]), int(year), list(map(int, time.split(':')))
calendar = {
    'January': 31, 'February': 28, 'March': 31,
    'April': 30, 'May': 31, 'June': 30, 'July': 31,
    'August': 31, 'September': 30, 'October': 31,
    'November': 30, 'December': 31,
}
current_month = 0

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    calendar['February'] += 1

for key, value in calendar.items():
    if key == month:
        break
    current_month += value

year_total_time = sum(calendar.values()) * 24 * 60
current_total_time = (current_month + day - 1) * 24 * 60 + time[0] * 60 + time[1]

print(current_total_time / year_total_time * 100)

