# 백준 - 브론즈2 - 대표값 - 2592 - 단순 구현, 수학 문제
'''
단순 구현, 수학 문제

평균값과, 입력으로 들어오는 값 중 제일 많이 등장하는 값을 출력하면 되는 간단한 문제이다.
평균값을 출력할 때 몫을 출력해야 한다. (단순한 '/'로 했다가 틀렸다..)
'''

n_list = [int(input()) for _ in range(10)]

# n_list = [10, 40, 30, 60, 30, 20, 60, 30, 40, 50] # 37  \  30

medium = sum(n_list) // 10
mode = max(n_list, key=n_list.count)

print(medium)
print(mode)
