# 단어 수학 - 골드 4 - 1339 - 그리디
'''
그리디 문제이다.

각 자리수로 1의 자리, 10의 자리, 100의 자리 수를 계산 한 후에 (dict로)
9부터 1씩 빼면서 dict에 자리 수를 곱한 값으로 res에 더해준다.
'''
n = int(input())
words = [ input() for _ in range(n) ]

# 테스트
# n = 2
# words = [ 'AAA', 'AAA' ] # 1998
# n = 2
# words = [ 'GCF', 'ACDEB' ] # 99437
# n = 10
# words = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ] # 45
# n = 2
# words = [ 'AB', 'BA' ] # 187

res, num = 0, 9
dic = dict()

for i in words:
    square = len(i) - 1

    for j in i:
        if j in dic:
            dic[j] += pow(10, square)
        else:
            dic[j] = pow(10, square)
        square -= 1
dic = sorted(dic.values(), reverse=True)

for i in dic:
    res += i * num
    num -= 1

print(res)
