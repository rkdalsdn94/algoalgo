'''
in
    9
    (())())
    (((()())()
    (()())((()))
    ((()()(()))(((())))()
    ()()()()(()()())()
    (()((())()(
    ((
    ))
    ())(()
out
    NO
    NO
    YES
    NO
    YES
    NO
    NO
    NO
    NO
'''

t = int(input())

for _ in range(t):
    st = input()
    left_li, rigth_li = [], []

    for i in st:
        if i == '(':
            left_li.append(i)
        else:
            rigth_li.append(i)
        if len(left_li) < len(rigth_li):
            break
        
    if len(left_li) == len(rigth_li):
        print("YES")
    else:
        print("NO")