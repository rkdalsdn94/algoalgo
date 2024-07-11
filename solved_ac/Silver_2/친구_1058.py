# 백준 - 실버2 - 친구 - 1058 - 그래프, 완전 탐색, 플로이드 와샬 문제
'''
그래프, 완전 탐색, 플로이드 와샬 문제

풀이 과정
1. 입력값을 받는다.
    - n: 그래프의 크기(사람 수)를 입력받는다.
    - graph: n개의 문자열을 입력받아 2차원 리스트로 저장한다.
2. 2차원 리스트(graph)를 초기화한다.
    - 각 사람이 자기 자신과의 거리는 0으로 설정한다.
    - ‘N’을 1000000으로, ‘Y’를 1로 변환하여 그래프를 구성한다.
3. 플로이드-와샬 알고리즘을 사용하여 모든 쌍의 최단 거리를 계산한다.
    - 3중 반복문을 통해 각 노드 쌍의 최단 경로를 업데이트한다.
4. 각 사람마다 2단계 이내의 친구 수를 계산한다.
    - 모든 사람을 순회하며 2단계 이내로 연결된 친구 수를 세고, 최대값을 갱신한다.
5. 최종 결과를 출력한다.
    - 2단계 이내로 연결된 친구 수 중 최대값을 출력한다.
'''

n = int(input())
graph = [list(input()) for _ in range(n)]

# 테스트
# n = 5
# graph = [
#     list('NYNNN'), list('YNYNN'), list('NYNYN'), list('NNYNY'), list('NNNYN')
# ] # 4
# n = 10
# graph = [
#     list('NNNNYNNNNN'), list('NNNNYNYYNN'), list('NNNYYYNNNN'),
#     list('NNYNNNNNNN'), list('YYYNNNNNNY'), list('NNYNNNNNYN'),
#     list('NYNNNNNYNN'), list('NYNNNNYNNN'), list('NNNNNYNNNN'),
#     list('NNNNYNNNNN')
# ] # 8
# n = 15
# graph = [
#     list('NNNNNNNNNNNNNNY'), list('NNNNNNNNNNNNNNN'), list('NNNNNNNYNNNNNNN'),
#     list('NNNNNNNYNNNNNNY'), list('NNNNNNNNNNNNNNY'), list('NNNNNNNNYNNNNNN'),
#     list('NNNNNNNNNNNNNNN'), list('NNYYNNNNNNNNNNN'), list('NNNNNYNNNNNYNNN'),
#     list('NNNNNNNNNNNNNNY'), list('NNNNNNNNNNNNNNN'), list('NNNNNNNNYNNNNNN'),
#     list('NNNNNNNNNNNNNNN'), list('NNNNNNNNNNNNNNN'), list('YNNYYNNNNYNNNNN')
# ] # 6

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif graph[i][j] == 'N':
            graph[i][j] = 1000000
        else:
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = 0
for i in range(n):
    temp = 0

    for j in range(n):
        if i != j and graph[i][j] <= 2:
            temp += 1

    res = max(res, temp)

print(res)
