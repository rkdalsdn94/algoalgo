# 백준 - 실버4 - 올바른 배열 - 1337 - 구현, 정렬, 투 포인터 문제
'''
구현, 정렬, 투 포인터 문제

보통 알고리즘을 풀 때 solved.ac 라는 곳을 통해서 문제 태그별로 푸는데, 해당 문제가 투 포인터 문제로 분류되어 있었다.
투 포인터 방식으로 어떻게 풀지? 라는 고민 때문에 더 고민하게 된 문제였다.
문제 분류에 크게 신경쓰지 않으면 좋을거 같지만서도, 분류를 통해 풀이법을 찾은 과정도 있어서... 그냥 문제를 더 많이 풀어보는 수 밖에 없을거 같다.

풀이 과정
1. input 값들을 잘 입력 받은 후 n_list는 정렬을 한다.
2. 정렬된 n_list의 값들을 하나 씩 꺼내면서 그 값의 5를 더한 범위로 2중 반복문을 만든다.
    2 번째 반복문의 시작값을 n_list에서 꺼낸 값의 1을 더한 값이므로 그 값들이 n_list에 담겨있는지 확인한다.
    담겨 있으면 5를 더한 범위를 넘지 않을 때까지 다음 숫자를 실행하고, 없으면 temp에 1을 더한다.
3. 2 번째 반복문을 다 돌고 난 후, 첫 번째 반복문 안에서 res와 값을 비교해 더 작은 값으로 바꿔준다.
4. res를 출력한다.
'''

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ])

# 테스트
n = 3
n_list = sorted([ 5, 6, 7 ]) # 2
# n = 6
# n_list = sorted([ 5, 7, 9, 8492, 8493, 192398 ]) # 2
# n = 4
# n_list = sorted([ 1000, 2000, 3000, 4000 ]) # 4
# n = 7
# n_list = sorted([ 6, 1, 9, 5, 7, 15, 8 ]) # 0

res = int(1e9)

for i in n_list:
    temp = 0

    for j in range(i + 1, i + 5):
        if j not in n_list:
            temp += 1
    res = min(temp, res)

print(res)