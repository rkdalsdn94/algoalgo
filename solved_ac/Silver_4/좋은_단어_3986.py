# 백준 - 실버4 - 좋은 단어 - 3986 - 자료 구조, 스택 문제
'''
자료 구조, 스택 문제

list를 이용해서 입력받은 문자의 마지막 글자와 그 전글자가 같으면 pop시킨 다음 list가 남아 있는지 check 하면 되는 문제이다.
'''

n = int(input())
res = 0

def stack_check(word, stack_list):
    for i in range(len(word)):
        stack_list.append(word[i])

        if len(stack_list) >= 2 and stack_list[-1] == stack_list[-2]:
            stack_list.pop()
            stack_list.pop()
    
    if stack_list:
        return False
    else:
        return True
    

for _ in range(n):
    word = input()
    stack_list = []

    if stack_check(word, stack_list):
        res += 1

print(res)
