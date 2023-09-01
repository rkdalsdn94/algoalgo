# 백준 - 실버5 - 미아 노트 - 20114 - 문자열 문제
'''
문자열 문제

세 개의 반복문을 이용해서 풀 수 있다. (아니면 제일 바깥의 반복문을 함수로
원래 문자열 만큼 반복하면서, 번진 범위로 반복한다.
번진 범위로 반복할 때 가로로 반복하면서 세로를 검사하면 된다.

가로로 번진 범위 즉, w 범위로 반복하면서 세로도 검사하는데, '?' 아닌 글자가 나오면 res에 추가한 뒤 flag 값을 바꿔 다음 글자를 검사한다.
가로 세로 모두 번진 범위가 '?'로 되어 있으면 res에 '?'를 추가한다.
최종적으로 res에 더해진 값을 출력하면 된다.

https://pythontutor.com/render.html#mode=display
위 링크에서 아레 테스트 부분을 한 스텝씩 돌리면 쉽게 이해할 수 있다.
'''

n, h, w = map(int, input().split())
word_list = [input() for _ in range(h)]

# 테스트
# n, h, w = 3, 2, 2
# word_list = [ 'a?????', '???bcc' ] # abc
# n, h, w = 6, 2, 3
# word_list = ['???rrruuu???ttt???', 'f?f?rruuu?????t???'] # fru?t?

res = ''

for i in range(n): # 문자열의 길이
    flag = False

    for j in range(i * w, (i + 1) * w): # 가로로 번진 범위 ex) w가 2일 때 0 -> 2 -> 4 이런 식으로 가로로 번짐 범위 만큼 반복해야 된다.
        for k in range(h): # 세로로 번진 범위 ex) 가로로 번진 범위 만큼 반복하는 중 세로에서 '?'가 아닌 글자가 있으면 res에 추가한다.
            if word_list[k][j] != '?':
                res += word_list[k][j]
                flag = True
                break
        if flag:
            break

    if flag:
        continue
    res += '?'

print(res)
