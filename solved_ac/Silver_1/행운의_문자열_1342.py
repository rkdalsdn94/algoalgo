# 백준 - 실버1 - 행운의 문자열 - 1342 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

수학적으로 풀면 더 빠르게 풀리는거 같다. (아래 코드로 제출했을 때 메모리와 시간은 각각 116768, 2592 이렇게 된다.)
아래 풀이는 완전 탐색과 백 트래킹으로만 풀었다.
    참고 링크
    - https://www.youtube.com/watch?v=LIBUyTyZ-F0
    - https://kimmeh1.tistory.com/355

풀이 과정
 - 입력으로 들어온 문자를 Counter를 활용해 키와 값을 가지는 딕셔너리 형태로 만들어준다.
 - 백 트래킹 함수를 만드는 데 2개의 인자가 필요하다.
    - 이전 값을 기억(중복방지)하기 위해 previous의 약자로 pre
    - 횟수를 체크하기 위한 cnt
    - cnt가 word의 길이와 같아졌을 때 res를 1 증가하고 종료한다.
    - Conter를 활용해 만든 temp의 키 값들만 꺼내서 이전 값과 같은지, temp의 해당 키의 숫자가 존재하는 지 검사한다.
    - 함수를 실행할 때 temp의 해당 키의 값을 1 빼고, 함수가 끝났을 때 1을 다시 더해준다.
 - 처음 빈 문자열과 0을 입력으로 주고 백 트래킹 함수를 실행한다.
'''

from collections import Counter

# word = list(input())

word = list('aabbbaa') # 1
# word = list('ab') # 2
# word = list('aaab') # 0
# word = list('abcdefghij') # 3628800

temp = Counter(word)
res = 0

def back_tracking(pre, cnt):
    global res

    if cnt == len(word):
        res += 1
        return

    for i in temp.keys():
        if i != pre and temp[i] > 0:
            temp[i] -= 1
            back_tracking(i, cnt + 1)
            temp[i] += 1

back_tracking('', 0)
print(res)
