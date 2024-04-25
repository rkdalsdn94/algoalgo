# 백준 - 실버1 - 에너지 모으기 - 16198 - 완전 탐색, 재귀, 백트래킹 문제
'''
완전 탐색, 재귀, 백트래킹 문제

처음엔 ck 변수로 방문 여부를 체크한 뒤 답을 구하는 식으로 계산했다.
하지만 이렇게 할 경우 n_list[i - 1] * n_list[i + 1] 의 값이 정확하지 않는다.
따라서, n_list의 인덱스 값을 삭제하는 방식으로 변경했다.

풀이 과정
 1. 입력을 받는다.
 2. 완전 탐색방식으로 백트래킹을 이용해 답을 구한다.
    2.1. n_list의 길이가 2가 되면 res와 비교하여 큰 값을 res에 저장한다.
    2.2. n_list의 길이가 2가 아니면서 중간 값을 제외(pop)하고 다른 값들을 백트래킹으로 구한다.
    2.3. 백트래킹이 끝나면 다시 n_list에 값을 넣어준다. (insert 함수를 이용해 해당하는 위치에 temp를 넣어준다.)
 3. res를 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 4
# n_list = [1, 2, 3, 4] # 12
# n = 5
# n_list = [100, 2, 1, 3, 100] # 10400
# n = 7
# n_list = [2, 2, 7, 6, 90, 5, 9] # 1818
# n = 10
# n_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 8

res = 0

def back_tracking(num):
    global res

    if len(n_list) == 2:
        res = max(res, num)
        return

    for i in range(1, len(n_list) - 1):
        energy = n_list[i - 1] * n_list[i + 1]
        temp = n_list.pop(i)
        back_tracking(num + energy)
        n_list.insert(i, temp)

back_tracking(0)
print(res)

'''
처음 틀린 풀이

ck = [0] * n

def back_tracking(num):
    global res

    if ck.count(1) == 2:
        res = max(res, num)
        return

    for i in range(1, n - 1):
        if ck[i] == 0:
            temp = n_list[i - 1] * n_list[i + 1]
            ck[i] = 1
            back_tracking(num + temp)
            ck[i] = 0

back_tracking(0)
print(res)
'''
