# 백준 - 실버5 - 키 큰 사람 - 11292 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

0이 나오기 전까지 반복문을 돌면서 주어진 입력값을 잘 입력 받고, max값을 출력하면 된다.

풀이 과정
1. n이 0이 들어오기 전까지 계속 while 문을 실행한다.
2. 입력된 값을 리스트에 담고 sorted 함수를 통해 split()된 1.** 문자로 역순으로 정렬을 진행한다.
3. 출력을 위한 res 변수에 역순으로 정렬된 n_list의 0번째 인자의 이름을 넣어준다.
4. 같은 값이 있는지 확인을 위해 1부터 n까지 반복문을 실행한다.
    4.1 같은 값이 있으면 res 리스트에 해당 값의 이름을 추가한다.
    4.2 같은 값이 없으면 반복문을 종료한다.
5. ' '.join 함수를 통해 띄어쓰기를 사이에 넣어준 뒤 출력한다.

in
    3
    John 1.75
    Mary 1.64
    Sam 1.81
    2
    Jose 1.62
    Miguel 1.58
    5
    John 1.75
    Mary 1.75
    Sam 1.74
    Jose 1.75
    Miguel 1.75
    0
out
    Sam
    Jose
    John Mary Jose Miguel
'''



while 1:
    n = int(input())

    if n == 0:
        break

    n_list = sorted([ input().split() for _ in range(n) ], key=lambda x: x[1], reverse=True)
    res = [n_list[0][0]]

    for i in range(1, n):
        if float(n_list[i][1]) != float(n_list[0][1]):
            break
        res.append(n_list[i][0])

    print(' '.join(res))
