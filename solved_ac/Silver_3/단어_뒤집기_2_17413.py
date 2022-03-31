'''
단순 구현 문제이다.
1. <> 안에 문자는 바꾸면 안돼서 '<' 가 나오면 flag를 False로 바꾼 다음 있는 그대로의 문자를 temp에 추가시켜 준 후
'>' 가 나왔을 때 flag를 다시 True로 바꾼 다음 res에 추가 한 후에 temp를 다시 빈 문자열로 만든다.

2. ' ' 가 나왔을 때 temp에 뒤집은 문자를 res에 추가한다.

3. '<', ' ' 가 아닐 때에는 문자를 뒤집으면서 temp에 추가한다.
'''

s = input()

# 테스트
# s = 'baekjoon online judge' # noojkeab enilno egduj
# s = '<open>tag<close>' # <open>gat<close>
# s = '<ab cd>ef gh<ij kl>' # <ab cd>fe hg<ij kl>
# s = 'one1 two2 three3 4fourr 5five 6six' # 1eno 2owt 3eerht rruof4 evif5 xis6
# s = '<int><max>2147483647<long long><max>9223372036854775807' # <int><max>7463847412<long long><max>7085774586302733229
# s = '<problem>17413<is hardest>problem ever<end>' # <problem>31471<is hardest>melborp reve<end>
# s = '<   space   >space space space<    spa   c e>' # <   space   >ecaps ecaps ecaps<    spa   c e>

temp = ''
flag = True
res = ''

for i in s:
    if flag:
        if i == '<':
            flag = False
            temp += i
        elif i == ' ':
            temp += i
            res += temp
            temp = ''
        else:
            temp = i + temp
    else:
        temp += i
        if i == '>':
            flag = True
            res += temp
            temp = ''

res += temp
print(res)
