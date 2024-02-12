# 백준 - 실버1 - 외계인의 기타 연주 - 2841 - 자료 구조(스택)
'''
자료 구조(스택) 문제

스택을 이용해 문제를 푸는데, 아래 코드에서 res를 1증가 시키는 부분이 손을 움직이는 부분이다.
https://pythontutor.com/render.html#mode=display 이 사이트에서 디버깅하는 것이 이해하는데 쉽다.

풀이 과정
 - 기타줄을 스택으로 두고(줄 입력 그대로 사용하기 위해 stack의 크기를 7로 잡는다) 이 stack을 이용해 답을 구해야 된다.
 - 그 다음 입력받은 n_list(줄과 프랫)의 값을 꺼내면서 다음의 과정을 진행한다.
    - 해당하는 기타줄(i)을 누른 적이 없다면
        - 해당 기타줄에 j를 list 형식으로 넣어주고, 손가락을 움직였으니 res를 1증가시칸다.
    - i번째 기타줄을 누른적이 있다면
            - while문을 사용한다. (while 조건으론 해당 기타줄이 눌러져있는지에 대한 여부)
            - 누른적이 있고, 해당하는 프렛(j)이 stack에 담겨있는 값보다 작으면 stack에서 값을 꺼내고, 손가락을 움직였으므로 res를 1 증가시킨다.
            - 프렛이 stack의 마지막 값과 같다면 while 문을 종료 시킨다.
            - 위 두 조건을 만족하지 못하면 stack에 append하고 res를 1 증가시키고, while 문을 break한다.
        - while 문이 다 끝나고 stack이 비어있다면 해당하는 프렛(j)를 stack에 추가하고, res를 1 증가시킨다.
 - 위 과정이 다 끝난 뒤 res를 출력하면 된다.
'''

n, p = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, p = 5, 15
# n_list = [[2, 8], [2, 10], [2, 12], [2, 10], [2, 5]] # 7
# n, p = 7, 17
# n_list = [[1, 5], [2, 3], [2, 5], [2, 7], [2, 4], [1, 5], [1, 3]] # 9

stack = [[] for _ in range(7)]
res = 0

for i, j in n_list:
    if stack[i]: # i번째 기타줄을 눌렀는지 검사
        while stack[i]:
            if j < stack[i][-1]:
                stack[i].pop()
                res += 1
            elif j == stack[i][-1]:
                break
            else:
                stack[i].append(j)
                res += 1
                break
        if not stack[i]:
            stack[i] = [j]
            res += 1
    else: # i번째 기타줄을 한 번이라도 누른 적이 없다면
        stack[i] = [j]
        res += 1

print(res)
