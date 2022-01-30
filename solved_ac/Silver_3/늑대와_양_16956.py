'''
울타리 수를 구하는 문제가 아니라고 표현되어 있다.
ㄴ> 예제 출력에 정확히 맞출 필요가 없다.
ㄴ> 단순하게 1번 예제에서 farm[4][1] 위치만 봐도 D가 되어 있다. (대각선으로 이동할 수 있는 경우가 없는데 D로 되어 있는거 보면 울타리를 심을 수 있으면 다 심어도 된다는 뜻인거 같다)
'''

r, c = map(int, input().split())
farm = [ list(input()) for _ in range(r) ]
'''
    테스트
r, c = 6, 6
farm = [ list('..S...'), list('..S.W.'), list('.S....'), list('..W...'), list('...W..'), list('......')] # 1 \n ..SD..   ..SDW.  .SD...  .DW...  DD.W..   ...... --> 울타리 수를 구하는게 아니다!
r, c = 1, 2
farm = [ list('SW')] # 0
r, c = 5, 5
farm = [ list('.S...'), list('...S.'), list('S....'), list('...S.'), list('.S...')] # 1 \n farm 을 출력하면 될 듯
'''
flag = False

for i in range(r):
    for j in range(c):
        if farm[i][j] == 'W':
            dx, dy = [1,0,-1,0], [0,1,0,-1]

            for ii, jj in zip(dx, dy):
                nx, ny = i + ii, j + jj

                if 0 <= nx < r and 0 <= ny < c and farm[nx][ny] == 'S':
                    flag = True
                    break
        
        elif farm[i][j] == '.':
            farm[i][j] = 'D'
        
        if flag: break
    
    if flag: break

if flag:
    print(0)
else:
    print(1)
    
    for i in farm:
        print(''.join(i))

