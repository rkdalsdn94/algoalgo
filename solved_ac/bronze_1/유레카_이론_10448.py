# 백준 - 브론즈1 - 유레카 이론 - 10448 - 수학, 완전 탐색 문제
'''
수학, 완전 탐색 문제

풀이 과정
 - 1 ~ 45까지의 삼각수를 리스트에 저장한다.
 - 1 ~ 45까지의 삼각수의 3개씩 더한 값이 1000보다 작으면 res 리스트에서 해당 값을 1로 바꾼다.
    - 세 숫자를 더하는 이유가 세 숫자의 조합으로 만들 수 있는 수이기 때문이다.
 - 입력으로 들어온 k를 res의 인덱스 값이 1인지 0인지 출력하면 된다.

in
    3
    10
    20
    1000
out
    1
    0
    1
'''

triangular_list = [i * (i + 1) // 2 for i in range(1, 46)] # 45번째 삼각수의 값이 1035 이므로 k의 값을 넘어간다.
res = [0] * 1001

for i in triangular_list:
    for j in triangular_list:
        for k in triangular_list:
            temp = i + j + k

            if temp <= 1000: # 세 숫자의 조합으로 만들 수 있는 수 중 1000보다 작으면 해당 인덱스의 값을 1 더한다.
                res[temp] = 1

t = int(input())

for _ in range(t):
    k = int(input())
    print(res[k])
