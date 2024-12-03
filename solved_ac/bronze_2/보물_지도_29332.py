# 백준 - 브론즈2 - 보물 지도 - 29332 - 구현 문제
'''
구현 문제

input으로 들어올 수 있는 값의 최댓값을 잘 생각해야 한다.
    - int(1e11)로 설정하면 된다. (10^11)
    - 이를 똑바로 확인안하고 습관적으로 int(1e9)로 설정했다가 꽤 많이 틀렸다. (이상한 부분을 수정하면서..)

풀이 과정
    1. 입력 받기
    2. 각 방향에 따라 l, r, u, d의 최소, 최대 값을 구해준다.
        2.1. l: x값이 최소
        2.2. r: x값이 최대
        2.3. u: y값이 최대
        2.4. d: y값이 최소
    3. 만약 l, r, u, d 값 중 초기값과 같다면 'Infinity' 출력
    4. 아니라면 넓이를 구해준다.
        4.1. 넓이 = (최대 - 최소 + 1) * (최대 - 최소 + 1)
'''

n = int(input())
command = [list(input().split()) for _ in range(n)]

# 테스트
# n = 4
# command = [
#     list('2 1 L'.split()), list('-2 -1 R'.split()),
#     list('0 -2 U'.split()), list('0 2 D'.split()),
# ] # 9
# n = 1
# command = [
#     list('1000000000 -1000000000 U'.split())
# ] # Infinity

l, r, u, d = int(1e11), -int(1e11), -int(1e11), int(1e11)

for x, y, direction in command:
    x, y = int(x), int(y)

    if direction == 'L':
        l = min(l, x)
    elif direction == 'R':
        r = max(r, x)
    elif direction == 'U':
        u = max(u, y)
    elif direction == 'D':
        d = min(d, y)

if l == int(1e11) or r == -int(1e11) or u == -int(1e11) or d == int(1e11):
    print('Infinity')
else:
    w, h = r - l + 1, u - d + 1
    print(w * h)
