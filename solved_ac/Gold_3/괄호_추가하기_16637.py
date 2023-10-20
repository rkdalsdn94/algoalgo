# 백준 - 골드3 - 괄호 추가하기 - 16637 - 구현, 완전 탐색, 재귀 문제
'''
구현, 완전 탐색, 재귀 문제

재귀 방식으로 입력으로 들어오는 수식을 완전 탐색하면서 풀었다.

풀이는 다른 블로그들이나 되게 유사해서 간단하게만 코드의 주석으로만 적으려고 한다.
대신 조심해야 할 부분으론 14%에서 '틀렸습니다.'가 나오면 음수 최저값을 안 했을 가능성이 높다.
https://www.acmicpc.net/board/view/57267 이 글을 통해 도움을 받았다.

res 초기값을 0으로 잡고 풀었었는데, 정답으로 음수가 나올 경우가 존재한다.
즉, 0보다 더 적은 수가 정답이 될 수 있으므로 res를 초기화할 때 조심해야 한다.

https://pythontutor.com/render.html#mode=display 해당 링크에서 코드를 한 단계식 확인해보는게 이해하는데 도움이 많이 된다.
'''

n = int(input())
nums = input()

# 테스트
# n = 9
# nums = '3+8*7-9*2' # 136
# n = 5
# nums = '8*3+5' # 64
# n = 7
# nums = '8*3+5+2' # 66
# n = 19
# nums = '1*2+3*4*5-6*7*8*9*0' # 0
# n = 19
# nums = '1*2+3*4*5-6*7*8*9*9' # 426384
# n = 19
# nums = '1-9-1-9-1-9-1-9-1-9' # 24

res = -int(1e9)

def calculation(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '*':
        return num1 * num2
    elif oper == '-':
        return num1 - num2

def recursive(idx, value):
    global res

    if idx == n - 1:
        res = max(res, value)
        return

    if idx + 2 < n: # 괄호를 생각하지 않고 단순 연산 과정
        recursive(idx + 2, calculation(int(value), nums[idx + 1], int(nums[idx + 2])))

    if idx + 4 < n: # 이 후에 오는 수에서 괄호를 추가한 상황 계산
        temp = calculation(int(nums[idx + 2]), nums[idx + 3], int(nums[idx + 4]))
        recursive(idx + 4, calculation(value, nums[idx + 1], temp))

recursive(0, int(nums[0]))

print(res)
