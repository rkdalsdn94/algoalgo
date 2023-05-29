# 백준 - 브론즈4 - 럭비 클럽 - 2083 - 단순 구현 문제
'''
단순 구현 문제

단순한 조건문으로 문제를 풀면 된다.
나이가 17보다 많거나 몸무게가 80kg 이상이면 Senior 그게 아니면 Junior를 출력하면 된다.

in
    Joe 16 34
    Bill 18 65
    Billy 17 65
    Sam 17 85
    # 0 0
out
    Joe Junior
    Bill Senior
    Billy Junior
    Sam Senior
'''

while 1:
    name, age, weight = input().split()
    age, weight = int(age), int(weight)

    if name == '#' and age == 0 and weight == 0:
        break

    if age > 17 or weight >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')
