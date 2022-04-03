'''
구현 문제,
bingo를 입력 받고, 리스트로 되어 있는 부르는 숫자를 입력 받는다.
대신 두번째에선 하나의 리스트로 받고, 해당 리스트에서 순차적으로 접근해 나간다.
(제일 처음 25번의 반복문에서 걸러질 수 있도록)

하나씩 부르면서 bingo_num이라는 변수에 빙고 한 줄이 완성 되었을 때 (조건문으로 빙고인지 탐색)
1씩 증가시켜 주면서, 3이 되면 flag로 모든 반복문을 종료 시킨다.

구현 문제를 풀면 풀수록 다양한 방식? 이 있는거 같다.
당분간 알고리즘은 구현 문제에 좀 더 초점을 맞추고 풀어야 될거 같다.
'''

bingo = [ list(map(int, input().split())) for _ in range(5) ]
call = list(map(int, input().split()))

for i in range(4):
    call.extend(list(map(int, input().split())))

# bingo = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], [22, 15, 7, 23, 18]]
# call = [5, 10, 7, 16, 2,
# 4, 22, 8, 17, 13,
# 3, 18, 1, 6, 25,
# 12, 19, 23, 14, 21,
# 11, 24, 9, 20, 15]

ck = [0] * 12
flag = False
bingo_num = 0

for i in range(25):
    if flag: break

    for j in range(5):
        if flag: break

        for z in range(5):
            if flag: break

            if call[i] == bingo[j][z]:
                bingo[j][z] = 0
                ck[j] += 1
                ck[z + 5] += 1

                if j == z: ck[10] += 1
                if j + z == 4: ck[11] += 1

            for d in range(12):
                if ck[d] == 5:
                    ck[d] = 0
                    bingo_num += 1

                    if bingo_num == 3:
                        flag = True
                        break

print(i)
