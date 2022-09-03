# 백준 실버4 - 수열 정리 - 1015 - 정렬 문제
'''
정렬 문제

입력받은 리스트(n_list) 하나 해당 리스트를 정렬한 리스트(sorted_list) 하나를 만든 후에 리스트의 길이(n)까지 반복문을 돈다.
원본 리스트의 각 원소들의 값이 정렬된 리스트의 몇 번째 인덱스인지 찾은 후에 해당 인덱스를 res에 추가 한다.
중복이 있을 수 있으므로 res에 추가한 정렬된 리스트의 원소값은 -1로 초기화 한다.(-1로 한 이유는 배열 A의 원소의 조건이 0번 부터 이므로)
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 3
# n_list = [2,3,1] # 1 2 0
# n = 4
# n_list = [2,1,3,1] # 2 0 3 1
# n = 8
# n_list = [4,1,6,1,3,6,1,4] # 4 0 6 1 3 7 2 5

sorted_list = sorted(n_list)
res = []

for i in range(n):
    res.append(sorted_list.index(n_list[i]))
    sorted_list[res[-1]] = -1

print(*res)
