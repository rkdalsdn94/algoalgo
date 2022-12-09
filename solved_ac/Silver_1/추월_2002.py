# 백준 - 추월 - 실버 1 - 2002 - 구현, 문자열 문제
'''
구현, 문자열 문제

문제 분류는 여러 가지가 있었는데, 여기서는 단순하게 풀었다.

풀이 과정
1. n, 진입하는 자동차(in_car_list), 나가는 자동차(out_car_list) 세 값을 잘 입력 받는다.
2. 출력할 때 사용할 res를 0으로 초기화한다.
3. n의 크기만큼 반복문을 시작한다.
    3.1. 현재(i) 나가는 차의 번호를 temp에 담는다.
    3.2. 들어온 차의 0번째와 맞지 않으면 res에 1을 더한다.
    3.3. 다음 순서를 비교하기 위해 들어온 차에서 현재 나간 차를 뺀다.
4. res를 출력한다.
'''

n = int(input())
in_car_list = [ input() for _ in range(n) ]
out_car_list = [ input() for _ in range(n) ]

# 테스트
# n = 4
# in_car_list = [ 'ZG431SN', 'ZG5080K', 'ST123D', 'ZG206A' ]
# out_car_list = [ 'ZG206A', 'ZG431SN', 'ZG5080K', 'ST123D' ] # 1
# n = 5
# in_car_list = [ 'ZG508OK', 'PU305A', 'RI604B', 'ZG206A', 'ZG232ZF' ]
# out_car_list = [ 'PU305A', 'ZG232ZF', 'ZG206A', 'ZG508OK', 'RI604B' ] # 3
# n = 5
# in_car_list = [ 'ZG206A', 'PU234Q', 'OS945CK', 'ZG431SN', 'ZG5962J' ]
# out_car_list = [ 'ZG5962J', 'OS945CK', 'ZG206A', 'PU234Q', 'ZG431SN' ] # 2

res = 0

for i in range(n):
    temp = out_car_list[i]

    if temp != in_car_list[0]:
        res += 1
    
    in_car_list.remove(temp)

print(res)
