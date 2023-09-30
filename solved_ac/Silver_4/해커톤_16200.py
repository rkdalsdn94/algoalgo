# 백준 - 실버4 - 해커톤 - 16200 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

입력으로 들어오는 n_list를 정렬 후
while 문을 통해 temp의 값이 n_list의 길이보다 커지기 전까지 아래 과정을 반복한다.
    res는 1씩 더하고, temp는 n_list의 값을 temp에 담아준다.
    단 temp에 담는 값을 n_list의 인덱스로 사용한다.
    뭔가 이 부분은 설명이 어려워 https://pythontutor.com/render.html#mode=display 여기서 돌려보면 금방 이해가 된다.

즉, 풀이의 핵심은 정렬 후 가장 가까운 값 끼리 묶어주면 된다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# n = 2
# n_list = sorted([2, 2]) # 1
# n = 5
# n_list = sorted([1, 2, 1, 2, 1]) # 4
# n = 5
# n_list = sorted([1, 2, 1, 2, 1]) # 4
# n = 9
# n_list = sorted([2, 2, 2, 3, 3, 3, 2, 2, 2]) # 4
# n = 9
# n_list = sorted([2, 2, 2, 2, 2, 3, 3, 3, 3]) # 4

res = 0
temp = 0

while temp < len(n_list):
    res += 1
    temp += n_list[temp]

print(res)

