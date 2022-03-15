'''
아래 주석 처리 한 부분이 처음 시도했다가 시간 초과가 나왔다.
n의 조건만 봐도 순열로 접근하면 안된다. 감이 잘 안와서 여러가지 검색 해보니
배수 판정법 이라는 걸 알게 됐고, 해당 판정법으로 문제를 풀었다. 링크(https://ko.wikipedia.org/wiki/배수_판정법)

30의 배수 : 30의 배수는 3의 배수이면서 일의 자리가 0인 수이다. (resverse=True 이유)
3의 배수 : 각 자리 숫자의 합이 3의 배수인 수이다.

위에 배수 판정법으로 문제를 풀면 된다.
'''

n = sorted(list(input()), reverse=True)

# 테스트
# n = sorted(list('30'), reverse=True) # 30
# n = sorted(list('102'), reverse=True) # 210
# n = sorted(list('2931'), reverse=True) # -1
# n = sorted(list('80875542'), reverse=True) # 88755420

res = int(''.join(n))

if n[-1] == '0' and res % 3 == 0:
    print(res)
else: print(-1)


## 아래 코드는 시간 초과가 나온다. n의 입력이 (10 ** 5)라서 시간초과가 나올거 같았다... 그래서 다시 풀기
# from itertools import permutations

# n = list(input())

# # 테스트
# # n = list('30') # 30
# # n = list('102') # 210
# # n = list('2931') # -1
# # n = list('80875542') # 88755420

# res = []

# for i in permutations(n, len(n)):
#     temp = ''.join(i)
#     if int(temp) % 30 == 0 and int(temp) != 0:
#         res.append(int(temp))

# if res: print(max(res))
# else: print(-1)
