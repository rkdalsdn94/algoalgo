# 백준 - 골드5 - 별 찍기 10 - 2447 - 분할 정복, 재귀 문제
'''
분할 정복, 재귀 문제

*** -> '*' * 3
* * -> '*' + ' ' * (n // 3) + '*'
*** -> '*' * 3
위 형식으로 재귀를 구하는데, 각 재귀의 반환을 list로 담은 후 해당 list에서 오른쪽 조건들을 재귀로 구현하면된다.
제일 아래 다른 정답도 보면 좋을거 같다. 푼 방식은 똑같은데 구현을 다르게 했다.

in
    27
out
    ***************************
    * ** ** ** ** ** ** ** ** *
    ***************************
    ***   ******   ******   ***
    * *   * ** *   * ** *   * *
    ***   ******   ******   ***
    ***************************
    * ** ** ** ** ** ** ** ** *
    ***************************
    *********         *********
    * ** ** *         * ** ** *
    *********         *********
    ***   ***         ***   ***
    * *   * *         * *   * *
    ***   ***         ***   ***
    *********         *********
    * ** ** *         * ** ** *
    *********         *********
    ***************************
    * ** ** ** ** ** ** ** ** *
    ***************************
    ***   ******   ******   ***
    * *   * ** *   * ** *   * *
    ***   ******   ******   ***
    ***************************
    * ** ** ** ** ** ** ** ** *
    ***************************
'''

n = int(input())

def recursive(n):
    if n == 1:
        return ['*']

    temp = recursive(n // 3)
    res = []
    for i in temp:
        res.append(i * 3)
    for i in temp:
        res.append(i + ' ' * (n // 3) + i)
    for i in temp:
        res.append(i * 3)

    return res

print('\n'.join(recursive(n)))

'''
다른 사람 코드중에 푼 방식은 똑같은데 *을 합치는 부분을 함수로 뺀 코드가 좋아서 참고용으로 적었다.

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
    return a + b + a
print('\n'.join(star10(int(input()))))
'''
