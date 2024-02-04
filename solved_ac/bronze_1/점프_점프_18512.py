# 백준 - 브론즈1 - 점프 점프 - 18512 - 수학, 완전 탐색, 구현 문제
'''
수학, 완전 탐색, 구현 문제

겹치지 않는 경우(-1이 되는 경우)를 어떻게 할 지가 관건이었다.
    - 완전 탐색으로 품 (200번 실행)

풀이 과정
    - 대략 1000번 정도 반복해도 같은 값이 안 나온다면 겹치는 수가 없지 않을까? 최대 횟수를 1000번으로 실행했더니 정답처리 되었다. (200번까지만 해도 통과가 됨)
 - 풀이는 단순하게 계속 p1, p2에 각각 x와 y를 더한 뒤 x_방문_체크_배열과, y_방문_체크_배열에 append 한 뒤 겹치는 값이 있을 때 p1과 p2 중 작은 값을 출력하면 된다.
 - 200번을 돌아도 프로그램이 exit 되지 않았다면 -1을 출력하면 된다.
'''

x, y, p1, p2 = map(int, input().split())

# 테스트
# x, y, p1, p2 = 10, 12, 30, 8 # 80
# x, y, p1, p2 = 1, 1, 7, 12 # 12
# x, y, p1, p2 = 7, 7, 2, 1 # -1

x_visited_list = [p1]
y_visited_list = [p2]

for _ in range(201):
    p1 += x
    p2 += y
    x_visited_list.append(p1)
    y_visited_list.append(p2)

    if p1 in y_visited_list or p2 in x_visited_list:
        print(min(p1, p2))
        exit(0)

print(-1)
