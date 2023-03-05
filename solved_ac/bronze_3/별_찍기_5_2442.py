# 백준 - 브론즈3 - 별 찍기 5 - 2442 - 구현 문제
'''
구현 문제

2 * n - 1의 범위로 별 찍기 문제이다.
문제에 답이 있다. 위 식으로 '*'을 표시하면 된다.

처음 제출 했을 때 res = space_bar + star + space_bar <-- 이렇게 출력했다가 출력 형식이 잘 못되었다는 오류가 나왔다. 
그래서 예제 출력에 있는 답을 드래그 해보니 뒤에는 공백이 제거된 상태여서 뒤 space_bar를 제거하니까 통과되었다.
'''

n = int(input())

# 테스트
# n = 5
'''
out
    *
   ***
  *****
 *******
*********
'''

for i in range(1, n + 1):
    space_bar = ''
    star = '*' * ((2 * i) - 1)

    for j in range(i + 1, n + 1):
        space_bar += ' '

    res = space_bar + star
    print(res)
