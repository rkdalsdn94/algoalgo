from collections import Counter

res = ''
word = Counter(input().upper()).most_common()
# 테스트
# word = Counter('Mississipi'.upper()).most_common()
# word = Counter('zZa'.upper()).most_common()
# word = Counter('z'.upper()).most_common()
# word = Counter('baaa'.upper()).most_common()
temp = word.pop(0)

for i, j in word:
    if temp[1] == j:
        res += '?'
        break
    break

if res == '?':
    print(res)
else:
    print(temp[0])

