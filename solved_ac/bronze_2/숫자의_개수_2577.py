'''
수학, 단순 구현

곱하고 count로 해당 수가 몇개 있는지 세면 된다. 단순 구현이다.
'''

a, b, c = int(input()), int(input()), int(input())

# 테스트
# a, b, c = 150, 266, 427 # 3, 1, 0, 2, 0 ,0 ,0, 2, 0, 0

res = str(a * b * c)

for i in range(10):
    print(res.count(str(i)))
