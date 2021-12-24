from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    # str1, str2 = re.sub('[^A-Z]', '', str1), re.sub('[^A-Z]', '', str2) # 여기서 문자로만 자르면 테케 3번에서 문제가 생김
    # print(str1, str2)
    union_list = []
    inter_list = []

    for i in range(1, len(str1)):
        # print(str1[i])
        if str1[i-1].isalpha() and str1[i].isalpha():
            union_list.append(str1[i-1] + str1[i])
    # print(union_list)

    for i in range(1, len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            inter_list.append(str2[i-1] + str2[i])
    # print(inter_list)

    union_answer = list((Counter(union_list) | Counter(inter_list)).elements())
    inter_answer = list((Counter(union_list) & Counter(inter_list)).elements())

    # print(union_answer, inter_answer, len(union_answer), len(inter_answer))

    if len(union_answer) == 0 and len(inter_answer) == 0:
        return 65536
    return int(len(inter_answer) / len(union_answer) * 65536)
    

print(solution('FRANCE', 'french')) # 16384
print(solution('handshake', 'shake hands')) # 65536
print(solution('aa1+aa2', 'AAAA12')) # 43690
print(solution('E=M*C^2', 'e=m*c^2')) # 65536
