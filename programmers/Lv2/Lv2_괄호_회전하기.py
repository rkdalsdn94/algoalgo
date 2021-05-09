def solution(s):
    answer = 0
    dic = {'[':']','(':')','{':'}'}

    for i in range(len(s)):
        st = list(s[i:] + s[:i])
        key = []

        while st:
            temp = st.pop(0)
            if not key:
                key.append(temp)
            else:
                if key[-1] in (']', ')', '}'):
                    break
                if dic[key[-1]] == temp:
                    key.pop()
                else:
                    key.append(temp)
        if not key:
            answer += 1

    return answer

print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]"))   # 0
print(solution("}}}"))    # 0