'''
1. 10진수 -> n진수 변환
2. 소수 찾기
위에 두 상황에서의 문제를 풀어봤으면 금방 풀 수 있다.
1번에 대해서 잘 모르겠으면 https://programmer-ririhan.tistory.com/161 여기 링크를 참고하자
해당 링크에서 while문을 하고 난 뒤에 temp = temp[::-1] 하는 부분이 없다. 이 부분을 해야 된다!
 ㄴ--> k의 범위가 최대 10이라서 while문으로 했지만, 만약 10진법 이후의 숫자에 대해서면 문자열을 정의해놓고 풀어야 된다.
        ㄴ--> convertString = '0123456789ABCDEF' 이런식으로 정의해놓고 해야된다.

진수 변환 후 문제 조건에서 0P0, P0, 0P 경우를 생각하라고 하는데,
각 자릿수에 0을 포함하지 않는 경우라고 해서 그냥 0으로 split 했다.
'''

def prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    temp = ''
    while n:
        temp += str(n % k)
        n //= k
    
    temp = temp[::-1].split('0')
    
    for i in temp:
        if len(i) >= 1 and prime_num(int(i)):
            answer += 1
    
    return answer

print(solution(437674, 3)) # 3
print(solution(110011, 10))  # 2
