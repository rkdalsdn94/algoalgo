'''
dp, 구현 문제

아이이러를 구현하는데 있어 감이 안와서 다른 사람들이 어떻게 풀었는지, 감을 잡으려고
https://www.hamadevelop.me/algorithm-n-expression/ 해당 블로그를 참고했다.
저 분의 블로그를 참고한 후에도 이해를 하는 과정까지도 시간이 꽤 걸린거 같다.
구현 문제에 좀 더 익숙해 져야 될거 같다.

처음 구상한 아이디어는 비슷하게 접근 했는데, 4중 반복으로 해결할 생각을 못했었다...
'''

def solution(N, number):
    S = [0, {N}]
    
    if N == number:
        return 1

    for i in range(2, 9):
        case = set()
        num = int(str(N) * i)
        case.add(num)

        for j in range(1, i // 2 + 1):
            for x in S[j]:
                for y in S[i - j]:
                    case.add(x + y)
                    case.add(x - y)
                    case.add(y - x)
                    case.add(x * y)

                    if y != 0: case.add(x // y)
                    if x != 0: case.add(y // x)

        if number in case:
            return i
        S.append(case)

    return -1

print(solution(5, 12)) # 4
print(solution(2, 11)) # 3