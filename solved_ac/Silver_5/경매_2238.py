# 백준 - 실버5 - 경매 - 2238 - 구현 문제
'''
구현 문제

처음에 딕셔너리를 활용해서 풀려고 했는데, 잘 안돼서 아래 코드를 참고했다.
https://recordofwonseok.tistory.com/424

따로 설명할 부분은 없지만 풀이 방식을 어떻게 생각해냐는게 관건인거 같다.
'''

u, n = map(int, input().split())
num_list = [0] * 10001
name_list = [ [] for _ in range(10001) ]
temp = 10001

for _ in range(n):
    a, b = input().split()
    b = int(b)
    name_list[b].append(a)
    num_list[b] += 1

for i in range(10001):
    if num_list[i] != 0:
        temp = min(temp, num_list[i])

for i in range(10001):
    if temp == num_list[i]:
        print(name_list[i][0], i)
        break