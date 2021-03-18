# 처음에 n_list를 list 로 받았다가 시간 초과 남
# 중복 제거 위해서 set자료형 사용
'''
input
5
4 1 5 2 3
5
1 3 7 9 5
out
1
1
0
0
1
'''
n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)


