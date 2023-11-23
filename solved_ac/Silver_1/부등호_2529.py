# 백준 - 실버1 - 부등호 - 2529 - 백 트래킹, 완전 탐색 문제
'''
백 트래킹, 완전 탐색 문제

기본적인 백트래킹 문제이지만 아직 백 트래킹 문제가 익숙하지 않아 그런지 시간이 오래 걸렸다.

0부터 9까지 숫자 리스트를 ck라는 이름으로 만들어 준다.
중복되는 숫자가 없어야 되므로 이 부분을 백 트래킹으로 처리한다.
또한 숫자를 대입했을 때 입력으로 들어오는 부등호와 맞는지 확인하기 위해 check 함수를 사용했다.

check 함수를 통해 두 숫자의 대입해서 부등호의 값이 참인지 거짓인지 판단한 뒤 참이면 해당 숫자를 사용중으로 표기하고,
recursive 함수를 재귀적으로 실행한다. (숫자를 사용하고, return 됐으면 해당 숫자를 반납해야 된다.)

재귀에 관련된 코드를 파악할 때 적당히 낮은 숫자를 손으로든,
https://pythontutor.com/visualize.html#mode=edit 여기 링크든 한 단계씩 확인해봐야 더 쉽게 이해할 수 있다.
'''

k = int(input())
sign_list = list(input().split())

# 테스트
# k = 2
# sign_list = ['<', '>'] # 897  \  021
# k = 9
# sign_list = ['>', '<', '<', '<', '>', '>', '>', '<', '<'] # 9567843012  \  1023765489

ck = [0] * 10
res = []

def check(x, y, z):
    if z == '<':
        return x < y
    return x > y

def recursive(depth, nums):
    if depth == k + 1:
        res.append(nums)
        return

    for i in range(10):
        if not ck[i] and (depth == 0 or check(nums[depth - 1], str(i), sign_list[depth - 1])):
            ck[i] = 1
            recursive(depth + 1, nums + str(i))
            ck[i] = 0

recursive(0, '')
print(res[-1])
print(res[0])
