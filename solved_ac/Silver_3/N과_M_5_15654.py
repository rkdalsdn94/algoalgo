# 백준 - 실버3 - N과 M 5 - 15654 - 백 트래킹 문제
'''
백 트래킹 문제

n과 m의 크기가 최대 8까지 밖에 안돼서 itertools 의 permutations 를 이용해 풀어도 된다.
백 트래킹 풀이도 파일 제일 아래 적어놨다.
'''

from itertools import permutations as permu

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# from itertools import combinations as combi
# n, m = 3, 1
# n_list = sorted([4, 5, 2]) # 2  \  4  \  5
# n, m = 4, 2
# n_list = sorted([9, 8, 7, 1])
# '''
#     1 7
#     1 8
#     1 9
#     7 1
#     7 8
#     7 9
#     8 1
#     8 7
#     8 9
#     9 1
#     9 7
#     9 8
# '''
# n, m = 4, 4
# n_list = sorted([1231, 1232, 1233, 1234])
# '''
#     1231 1232 1233 1234
#     1231 1232 1234 1233
#     1231 1233 1232 1234
#     1231 1233 1234 1232
#     1231 1234 1232 1233
#     1231 1234 1233 1232
#     1232 1231 1233 1234
#     1232 1231 1234 1233
#     1232 1233 1231 1234
#     1232 1233 1234 1231
#     1232 1234 1231 1233
#     1232 1234 1233 1231
#     1233 1231 1232 1234
#     1233 1231 1234 1232
#     1233 1232 1231 1234
#     1233 1232 1234 1231
#     1233 1234 1231 1232
#     1233 1234 1232 1231
#     1234 1231 1232 1233
#     1234 1231 1233 1232
#     1234 1232 1231 1233
#     1234 1232 1233 1231
#     1234 1233 1231 1232
#     1234 1233 1232 1231
# '''

for i in permu(n_list, m):
    print(*i)


'''
백 트래킹 풀이

백 트래킹 방식의 기본 구현이다. 재귀 함수를 이용해서 풀었다.

코드가 크게 어렵지 않아 간단한 설명만 적어보면,
    - ck 리스트를 활용해서 방문하지 않은 곳이면 방문했다는 표시를 남긴 채 재귀 함수를 실행한다.
    - 재귀 함수 안에서 word의 길이가 m이랑 같으면 word를 출력한다.
    - 재귀 함수 끝마다 방문했던 곳을 0으로 바꿔준다.
'''
n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
ck = [0] * n

def recursive(word, cnt):
    if cnt == m:
        print(word)
    for i in range(n):
        if not ck[i]:
            ck[i] = 1
            recursive(word + ' ' + str(n_list[i]), cnt + 1)
            ck[i] = 0

for i in range(n):
    ck[i] = 1
    recursive(str(n_list[i]), 1)
    ck[i]= 0
