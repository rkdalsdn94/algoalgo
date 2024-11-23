# 백준 - 브론즈1 - N 퍼즐 - 3041 - 구현 문제
'''
구현 문제

퍼즐을 완성하기 위해 움직여야 하는 횟수를 구하는 문제

풀이 과정
    1. 이상적인 퍼즐의 상태를 저장한다.
    2. 현재 퍼즐의 상태를 입력받는다.
    3. 이상적인 퍼즐과 현재 퍼즐을 비교하여 이동해야 하는 횟수를 구한다.
    4. 결과 출력
'''

ideal_puzzle = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
currnt_puzzle = [input() for _ in range(4)]

# 테스트
# currnt_puzzle = ['ABCD', 'EFGH', 'IJKL', 'M.NO'] # 2
# currnt_puzzle = ['.BCD', 'EAGH', 'IJFL', 'MNOK'] # 6

cnt = 0
temp = {}
for i in range(4):
    for j in range(4):
        if ideal_puzzle[i][j] != currnt_puzzle[i][j] and currnt_puzzle[i][j] != '.':
            temp[currnt_puzzle[i][j]] = (i, j)

for i in range(4):
    for j in range(4):
        if ideal_puzzle[i][j] in temp.keys():
            cnt += abs(temp[ideal_puzzle[i][j]][0] - i) + abs(temp[ideal_puzzle[i][j]][1] - j)
print(cnt)
