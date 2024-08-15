# 백준 - 실버3 - 캠프파이어 - 3018 - 구현, 자료 구조(해시) 문제
'''
구현, 자료 구조(해시) 문제

풀이 과정
    1. 입력을 받는다.
    2. res를 만들어 각각의 값을 set()으로 초기화한다.
    3. e_list를 돌면서 1이 있는지 확인한다.
        3.1. 1이 있다면 res에 추가하고, 다음 곡으로 넘어간다.
        3.2. 1이 없다면 temp을 만들어서 temp과 res를 합친다. (temp = res[1] | res[j] 또는 union 사용)
    5. res의 keys를 꺼내 1번째 값과 비교하여 같으면 출력한다.
'''

n = int(input())
e = int(input())
e_list = [list(map(int, input().split())) for _ in range(e)]

# 테스트
# n = 4
# e = 3
# e_list = [
#     [2, 1, 2], [3, 2, 3, 4], [3, 4, 2, 1]
# ] # 1  \  2  \  4
# n = 8
# e = 5
# e_list = [
#     [4, 1, 3, 5, 4], [2, 5, 6],
#     [3, 6, 7, 8], [2, 6, 2], [4, 2, 6, 8, 1]
# ] # 1  \  2  \  6  \  8
# n = 5
# e = 3
# e_list = [
#     [2, 1, 3], [2, 2, 1], [4, 2, 1, 4, 5]
# ] # 1

res = dict()
for i in range(1, n + 1):
    res[i] = set()

song_num = 1

for i in e_list:
    k, arr = i[0], i[1:]

    if 1 in arr:
        for j in arr:
            res[j].add(song_num)
        song_num += 1
    else:
        temp = set()

        for j in arr:
            temp = temp | res[j] # temp.union(dict[j])
        for j in arr:
            res[j] = res[j] | temp # temp.union(dict[j])

for i in res.keys():
    if res[i] == res[1]:
        print(i)
