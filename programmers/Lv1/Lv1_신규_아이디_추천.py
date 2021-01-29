import re


def solution(new_id):
    answer = [i for i in new_id.lower() if i.isalnum() or i ==
              '-' or i == '_' or i == '.']  # 1
    answer = list(re.sub('[..]+', '.', ''.join(answer)))  # 2
    # print(answer)
    # 4
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if not answer:
        answer.append('a')
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[0] == '.':
            answer = answer[1::]
        elif answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))

    return ''.join(answer)


print(solution("...!@BaT#*...y.abcdefghijklm")
      == 'bat.y.abcdefghi')  # bat.y.abcdefghi
print(solution("z-+.^.") == 'z--')     # z--
print(solution("=.=") == 'aaa')    # aaa
print(solution("123_.def") == '123_.def')   # 123_.def
print(solution("abcdefghijklmn.p") == 'abcdefghijklmn')  # 'abcdefghijklmn'
