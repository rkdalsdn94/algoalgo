# 백준 - 브론즈1 - 싸이클 - 2526 - 구현 문제
'''
구현 문제

문제가 쉬워서 방심하다 틀렸다. (전에도 그랬지만 지문을 제대로 이해하고 푸는게 중요하다고 느꼈다.)

만약, 55%에서 틀린다면 아래 부분을 주의하자.
지문중에 다음과 같은 부분이 있다.
'N = 9, P = 3을 가지고 시작하면, 9×9 = 81이고 3으로 나눈 나머지는 0이며, 0×3 = 0이고 3으로 나눈 나머지도 0이기 때문에 처음 9를 제외하면 0이 무한히 반복되게 된다.'

즉, n이 4이고 p가 96일 때를 생각해보면 된다. 16 빼고는 64 때부터 중복되는 값이라 1을 출력해야 되는데, 이 부분을 생각하지 않으면 2가 나와서 틀리게 된다.
    1. new_n = (4 * 4) % 96 = 16
    2. new_n = (16 * 4) % 96 = 64
    3. new_n = (64 * 4) % 96 = 64 --> 64 가 중복되는 값이라 16만 싸이클이 발생하지 않는다. 즉, 64 부터 싸이클 발생했다. 이 부분을 주의해야 한다.

위에 말한 부분만 생각한 뒤 문제를 풀면된다.  len(res) - res.index(new_n)  이렇게 해결할 수 있다. 중복이 발생하는 부분의 인덱스 값을 빼고 출력하면 된다.
'''

n, p = map(int, input().split())

# 테스트
# n, p = 67, 31 # 3
# n, p = 96, 61 # 60
# n, p = 9, 3 # 1
# n, p = 4, 96 # 1

original_n = n
res = []

while 1:
    new_n = (n * original_n) % p

    if new_n in res:
        print(len(res) - res.index(new_n)) # res.index(new_n) 을 빼지 않으면 55%에서 틀린다.
        exit(0)
    res.append(new_n)
    n = new_n
