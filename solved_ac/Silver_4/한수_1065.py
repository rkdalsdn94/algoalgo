'''
100의 자릿수까지만 생각하면 되는 문제이다. (n의 조건이 1000까지라서.. 1000은 한수가 되지 못한다...)
조금만 생각해 보면 100 이전까지의 수는 모두 1이나 0으로 일정하다.
100이 넘으면 100부터 n까지 자릿수의 차이를 계산해 주면 된다 (n_list[0] - n_list[1] == n_list[1] - n_list[2] 여기 부분)
100의 자리까지만 생각하면 될 거 같아서 그 이후 인덱스[3]는 계산하지 않았다.
'''

# n = int(input())

# 테스트
# n = 110 # 99
# n = 1 # 1
n = 210 # 105
# n = 1000 # 144
# n = 500 # 119

def hansu(n: int):
    res = 99

    for i in range(100, n + 1):
        n_list = list(map(int, str(i)))
        # print(n_list)
        
        if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            res += 1

    return res

if n < 100:
    print(n)
else:
    print(hansu(n))

