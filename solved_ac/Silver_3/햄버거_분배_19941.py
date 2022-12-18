# 백준 - 실버3 - 햄버거 분배 - 19941 - 그리디 문제
'''
그리디 문제

그리디 하게 접근하면 된다. P가 나왔을 때 word에서 가장 가까운 인덱스에 있는 햄버거를 먹으면 된다.
처음에 범위 조건만 생각해서 두 번째 반복문 때 이렇게 반복 조건문을 이렇게 했었는데 인덱스 에러가 났다. (i - k, i + k + 1)
생각해 보니 처음 시작하는 부분인 i - k의 범위는 음수가 나와서 값이 이상해질 가능성이 있고, 도착하는 i + k + 1의 범위가 n의 크기를 넘을 수도 있다.
따라서, max와 min을 활용해 범위 조건을 다시 세우니 통과되었다.

풀이 과정
1. input을 잘 입력받는다.
2. 전체 크기인 n 만큼 반복하면서 word의 글자가 'P'가 나오면 2번째 반복문을 실행한다.
    2.1. 2번째 반복 문의 범위는 처음에 i - k와 0 중 큰 값을 시작으로 하고, i + k + 1과 n 중 작은 값까지 실행하면 된다.
    2.2. 2번째 반복 문의 범위를 돌면서 해당 글자가 'H'가 나오면 햄버거를 먹을 수 있는 상황이므로 res를 1로 바꾼 후, 해당 글자를 0으로 초기화한다.
    2.3. 위 과정을 n의 크기만큼 반복하면서 값을 도출하면 된다.
3. res를 출력한다.
'''

n, k = map(int, input().split())
word = list(input())

# 테스트
# n, k = 20, 1
# word = list('HHPHPPHHPPHPPPHPHPHP') # 8
# n, k = 20, 2
# word = list('HHHHHPPPPPHPHPHPHHHP') # 7
res = 0

for i in range(n):
    if word[i] == 'P':
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if word[j] == 'H':
                res += 1
                word[j] = 0
                break

print(res)
