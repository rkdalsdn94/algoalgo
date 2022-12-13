# 백준 - 세 개의 소수 문제 - 11502 - 실버4 - 완전 탐색, 수학, 에토테네스의 체 문제
'''
완전 탐색, 수학, 에토테네스의 체 문제

문제에서 주어진 소수의 범위가 1000까지 이므로 해당 번째까지 소수를 미리 구한 다음
해당 소수 리스트를 3중 반복문으로 세 수의 합이 k와 같으면 해당 수를 출력한 후 다음 테스트 케이스를 실행하면 된다.
문제에서 '여러 개의 답이 가능하다면 그 중 하나만 출력하면 되고, 만약 불가능하다면 0을 출력한다.' 이런 조건이 있기 때문에 가능하다.

풀이 과정
1. k의 최대 범위인 1000까지 소수를 미리 구한다. -> prime_num_list 라는 이름의 배열
2. 테스트 케이스인 t를 입력받고 t만큼 반복문을 실행한다.
3. t반복문 안에서 각각 반복문이 시작할 때 k를 입력받고 flag를 False로 초기화 시킨다.
4. prime_num_list를 하나 씩 꺼내면서 3중 반복문을 실행한다.
5. 3중 루프 안에서 세 수의 합이 k가 될 때 해당 수(i, j, z)를 출력하고 flag를 True로 바꾼다.
6. flag가 True면 나머지 반복문을 다 멈추고 다음 t를 실행한다.

in
    3
    7
    11
    25
out
    2 2 3
    2 2 7
    5 7 13
'''

prime_num_list = []
for i in range(2, 1001):
    flag = True

    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    
    if flag:
        prime_num_list.append(i)

t = int(input())
for _ in range(t):
    k = int(input())
    flag = False
    
    for i in prime_num_list:
        for j in prime_num_list:
            for z in prime_num_list:
                if i + j + z == k:
                    print(i, j, z)
                    flag = True
                    break
            if flag: break
        if flag: break
