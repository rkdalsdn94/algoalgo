# 백준 - 숫제세는 양 (Small) - 14381 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

생각보다 까다로운 문제였다.
구현 방식은 다음과 같다. (테스트 케이스를 반복하는 부분은 생략)
    1. 처음 입력받은 n을 기억하기 위해 initial_n 이라는 이름으로 n을 int형으로 형 변환한 후 그 값을 대입시켜 둔다.
    2. 1 ~ 10 까지의 수가 중복없이 잘 들어왔는지 체크하기 위해 set 자료구조를 활용한 빈 temp 를 만한다.
    3. 입력받은 n이 0이면 어떤 방법을 사용하던 1 ~ 10까지 못 만드므로 0일 경우 INSOMNIA 를 출력하고 다음 단계를 실행하기 위해 continue를 사용한다.
    4. 0이 아닐경우 temp 의 길이가 10이 될 때까지 다음의 과정을 반복한다.
        4.1. 문자열로 구성된 n을 반복하면서 각 글자를 temp에 숫자형으로 바꾼 뒤 추가한다.
        4.2. 마지막 정답으로 출력하기 위해 res에 값을 n으로 만든다.
        4.3. 기존의 n을 int형으로 바뀐 뒤 처음 초기화한 initial_n 을 더한다. (문제에 있는 N, 2 × N, 3 × N 이걸 구현하기 위해)
    5. f 스트링을 활용해서 정답을 출력한다.


in
    4
    0
    1
    2
    11
out
    Case #1: INSOMNIA
    Case #2: 10
    Case #3: 90
    Case #4: 110
'''

t = int(input())

for i in range(1, t + 1):
    n = input()
    initial_n = int(n)
    temp = set()
    res = ''

    if n == '0':
        res = 'INSOMNIA'
        print(f'Case #{i}: {res}')
        continue

    while len(temp) != 10:
        for j in n:
            temp.add(int(j))
        res = n
        n = str(int(n) + initial_n)

    print(f'Case #{i}: {res}')
