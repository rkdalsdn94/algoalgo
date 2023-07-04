# 백준 - 브론즈2 - 백설 공주와 일곱 난쟁이 - 3040 - 완전 탐색 문제
'''
완전 탐색 문제

9개의 수를 갖는 n_list 에서 두 값을 뺏을 때 n_list의 전체 합이 100이 되는 걸 찾으면 된다.
두 값을 빼는 방법은 n_list의 9^2 범위로 for 문을 만든다. 
n_list 전체 합에서 i번째 인덱스와 j번재 인덱스의 값을 뺀다.
    단, 두 값의 인덱스가 서로 같을 때는 무시해야 된다. ( i == j면 continue )
i 번째 인덱스와 j 번째 인덱스의 값을 뺏을 때 100이 나오면 반복문을 종료하고, 해당 인덱스를 n_list에서 pop한 후 출력하면 된다.
'''

n_list = [ int(input()) for _ in range(9) ]

# 테스트
# n_list = [7, 8, 10, 13, 15, 19, 20, 23, 25] # 7  \  8  \  10  \  13  \  19  \  20  \  23
# n_list = [8, 6, 5, 1, 37, 30, 28, 22, 36] # 8  \  6  \  5  \  1  \  30  \  28  \  22

flag = False

for i in range(9):
    for j in range(9):
        if i == j:
            continue

        if sum(n_list) - n_list[i] - n_list[j] == 100:
            flag = True
            break
    if flag: break

n_list.pop(i)
n_list.pop(j - 1)
print('\n'.join(map(str, n_list)))
