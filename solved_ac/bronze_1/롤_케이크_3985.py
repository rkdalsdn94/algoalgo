# 백준 - 브론즈 1 - 롤 케이크 - 3985 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

문제의 난이도가 브론즈1 이라서 방식하고 막 제출했다가 2번 틀렸다..
틀린 이유는 첫 번째 출력에서 '가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호를 출력한다.'
방청객의 번호를 출력한게 아니라 길이를 출력해버렸다.. 위 부분을 수정하고 제출했더니 통과했다.

구현의 난이도는 어렵지 않는데, 문제의 대한 이해와 어렵진 않아도 시뮬레이션을 돌려본 후에 제출해야 될 거 같다.

아래에 있는 예제들을 https://pythontutor.com/visualize.html#mode=display 한 단계 씩 실행해보면 금방 이해할 수 있따.

in
    10
    3
    2 4
    7 8
    6 9
out
    3
    1

in
    10
    3
    1 3
    5 7
    8 9
out
    1
    1

in
    10
    5
    1 1
    1 2
    1 3
    1 4
    7 8
out
    4
    5
'''


l = int(input())
cake_list = [0] * (l + 1)
n = int(input())
temp = 0
wanted_max_audience = 0 # 첫 번째 정답을 위한
real_max_audience = [] # 실제로 가장 많은 조각을 받은 방청객의 번호를 위한

for i in range(1, n + 1):
    a, b = map(int, input().split())

    if temp < b - a + 1:
        wanted_max_audience = i
    temp = max(temp, b - a + 1)

    for j in range(a, b + 1):
        if not cake_list[j]:
            cake_list[j] = i

for i in range(1, n + 1):
    real_max_audience.append(cake_list.count(i))

print(wanted_max_audience)
print(real_max_audience.index(max(real_max_audience)) + 1)
