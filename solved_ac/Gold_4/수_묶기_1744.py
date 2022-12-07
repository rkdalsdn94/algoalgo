# 백준 - 수 묶기 - 골드4 - 1744 - 그리디, 정렬, 많은 조건 분기
'''
그리디, 정렬, 많은 조건 분기

음수(negative), 양수(positive) 리스트를 따로 만들고 난 다음
수를 입력받을 때 음수(0포함)인지 양수(1제외)인지 파악 후 각 리스트에 append 한다.
그다음 while 문과 조건문을 활용해서 계산하면 된다.

풀이 과정.
1. n을 입력 받고, 0을 포함한 음수를 담을 리스트와 1을 제외한 양수를 담을 리스트를 빈 리스트로 만들어 준다.
2. 정답을 출력할 res를 0으로 초기화한다.
3. n만큼 반복하면서 1이면 res에 1을 더하고, 0을 포함한 음수면 음수 리스트, 1을 제외한 양수를 양수 리스트에 append 한다.
4. 음수 리스트는 오름차순으로 정렬하고, 양수 리스트는 내림차순으로 정렬한다. -> 그래야 두 리스트 다 0번째 인덱스, 1번째 인덱스로 비교할 수 있다.
    ㄴ> 둘 다 오름차순으로 한 후에 양수에서 -1, -2 로 접근해도 똑같은데 0, 1로 통일하기 위해 양수 리스트는 내림차순으로 정렬했다.
5. 각각 리스트의 값이 있으면 빈 리스트가 될 때까지 while을 실행한다.
    5.1. 음수 리스트가 빈 리스트가 될 때까지 반복.
        5.1.1. 음수 리스트의 길이가 2보다 크거나 같으면 오름차순으로 정렬되어 있으므로 0번째와 1번째를 곱한 값을 res에 더한 다음 pop해준다.
        5.1.2. 길이가 2보다 작으면 값을 꺼낸 다음 res에 더한다.
    5.2. 양수 리스트가 빈 리스트가 될 때까지 반복. -> 5.1을 똑같이 실행하면 된다.
        5.2.1. 양수 리스트의 길이가 2보다 크거나 같으면 내림차순으로 정렬되어 있으므로 0번째와 1번째를 곱한 값을 res에 더한 다음 pop해준다.
        5.2.2. 길이가 2보다 작으면 값을 꺼낸 다음 res에 더한다.
6. res를 출력한다.

in
    4
    -1
    2
    1
    3
out
    6

in
    6
    0
    1
    2
    4
    3
    5
out
    27

in
    1
    -1
out
    -1

in
    3
    -1
    0
    1
out
    1

in
    2
    1
    1
out
    2
'''

n = int(input())
negative_list, positive_list = [], []
res = 0

for _ in range(n):
    x = int(input())

    if x < 1:
        negative_list.append(x)
    elif x == 1:
        res += 1
    else:
        positive_list.append(x)

negative_list.sort(); positive_list.sort(reverse=True);

while negative_list:
    if len(negative_list) >= 2:
        res += negative_list[0] * negative_list[1]
        negative_list.pop(0)
        negative_list.pop(0)
    else:
        res += negative_list.pop(0)

while positive_list:
    if len(positive_list) >= 2:
        res += positive_list[0] * positive_list[1]
        positive_list.pop(0)
        positive_list.pop(0)
    else:
        res += positive_list.pop(0)

print(res)