# 백준 - 브론즈1 - 일곱 난쟁이 - 2309 - 단순 구현, 완전 탐색, 정렬 문제
'''
단순 구현, 완전 탐색, 정렬 문제

9개의 숫자를 리스트에 담으면서 입력받고 오름차순 정렬을 한다.
해당 리스트에 전체 합(temp)에서 완전 탐색(이중 for 문)으로 숫자 두 개를 뺀다.
전체 합에서 숫자 두 개(i, j)씩 뺏을 때 값이 100 이 되면 해당 숫자 두 개를 리스트에서 제거하고 하나 씩 출력하면 된다.

*다른 사람 풀이를 보니까 combinations을 활용해서 푼거도 보이는데 해당 방법이 더 좋은거 같다.
'''

n_list = sorted([ int(input()) for _ in range(9) ])

# 테스트
# n_list = sorted([ 20, 7, 23, 19, 10, 15, 25, 8, 13 ]) # 7  \  8  \  10  \  13  \  19  \  20  \  23

temp = sum(n_list)
flag = False

for i in range(9):
    for j in range(i + 1, 9):
        if temp - (n_list[i] + n_list[j]) == 100:
            n_list.remove(i)
            n_list.remove(j)
            flag = True
            break
    if flag:
        break

for i in n_list:
    print(i)
