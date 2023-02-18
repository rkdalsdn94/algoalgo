# 백준 - 실버4 - 박 터뜨리기 - 19939 - 수학, 그리디 문제
'''
수학, 그리디 문제

수학적으로 구한 문제를 코드로 구하면 되는 문제이다.
가우스 덧셈 공식을 이용해서 해당 합이 n보다 크면 -1을 출력하고,
(n - 전체 합) % k 을 했을 때 나머지가 0이라면 k - 1을 출력하고, 나머진 k를 출력하면 된다.
'''

n, k = map(int, input().split())

# 테스트
# n, k = 5, 3 # -1
# n, k = 6, 3 # 2

gauss_add_principle = k * (k + 1) // 2

if gauss_add_principle > n:
    print(-1)
elif (n - gauss_add_principle) % k == 0:
    print(k - 1)
else:
    print(k)
