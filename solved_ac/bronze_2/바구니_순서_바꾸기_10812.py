# 백준 - 브론즈2 - 바구니 순서 바꾸기 - 10812 - 단순 구현, 시뮬레이션 문제
'''
단순 구현, 시뮬레이션 문제

왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 회전시키는데,
그 때 기준 바구니는 k번째 바구니라는 뜻이다

구현하는 거보다 문제를 해석할 때 어려움을 더 컸던 문제이다.
문제 해석만 끝나면 다음 풀이는 리스트 슬라이싱을 이용해 쉽게 풀 수 있다. (이 전에 풀었던 '백준 - 카드 역배치(10804)'문제랑 비슷)
start(i), end(j), mid(k) 가 주어질 때, start ~ mid와 mid ~ end의 인덱스 위치를 바꾸면 되는 문제이다.
단, start와 end의 각각의 값이 0과 n - 1이 아니므로 start 보다 작은 값과 end 보다 큰 값을 생각해야 된다. -> n_list[:i - 1], n_list[j:]
나머지 start부터 mid 까지 스왑하는 부분은 다음과 같다.
start부터 mid 까지 -> n_list[i - 1:k - 1]
mid부터 start 까지 -> n_list[k - 1:j]
상술한 두 부분의 순서를 바꿔줘야 되므로 mid ~ start 까지 + start ~ mid 까지 이렇게 더해줘야 한다.
'''

n, m = map(int, input().split())
n_list = [ i for i in range(1, n + 1) ]
m_list = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 10, 5
# n_list = [1,2,3,4,5,6,7,8,9,10]
# m_list = [ [1,6,4], [3,9,8], [2, 10, 5], [1,3,3], [2,6,2] ] # 1 4 6 2 3 7 10 5 8 9

for command in m_list:
    i, j, k = command
    # print(n_list[:i - 1], n_list[k - 1:j], n_list[i - 1:k - 1], n_list[j:])
    n_list = n_list[:i - 1] + n_list[k - 1:j] + n_list[i - 1:k - 1] + n_list[j:]

print(*n_list)
