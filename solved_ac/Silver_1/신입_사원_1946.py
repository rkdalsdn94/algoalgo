'''
python의 정렬(sorted, sort)을 사용할 때 원소가 2개 이상이면 0번째 원소가 기준이 돼서 정렬이 된다.
해당 문제 기준으론 서류심사 성적를 기준으로 정렬을 한 후, 면접 성적으로 비교를 해서 풀었다.
temp에 1명은 담고 시작하니까 res를 1로 두고 더해갔다.

sys.stdin.readline 을 하지 않으면 시간 초과가 난다.(python3, pypy3 둘 다 시간 초과)

in
    2
    5
    3 2
    1 4
    4 1
    2 3
    5 5
    7
    3 6
    7 3
    4 2
    1 4
    5 7
    2 5
    6 1
out
    4
    3
'''
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    people = sorted([ list(map(int, input().split())) for _ in range(n) ])
    # print(people)
    temp = people[0][1]
    res = 1

    for i in range(1, n):
        if temp > people[i][1]:
            res += 1
            temp = people[i][1]
    
    print(res)
