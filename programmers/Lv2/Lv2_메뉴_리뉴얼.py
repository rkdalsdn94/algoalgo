'''
    문제 푸는데 밑에 방식으로 풀었다가,
    다른 사람 풀이에 너무 괜찮은 방식이 있어 공부할겸 가져왔다
'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course:
        temp = []

        for order in orders:
            for j in combinations(sorted(order), i):
                # print(''.join(j))
                temp.append(''.join(j))
        
        sorted_temp = Counter(temp).most_common()
        answer += [food for food, cnt in sorted_temp if cnt >= 2 and cnt == sorted_temp[0][1]]

    return sorted(answer)

# def solution(orders, course):
#     answer = []
#     temp = [{} for _ in range(11)]
#     cnt_temp = [0 for _ in range(11)]

#     for order in orders:
#         for cnt in range(2, len(order) + 1):
#             for i in combinations(sorted(order), cnt):
#                 menu = ''.join(i)
#                 if menu in temp[cnt]:
#                     temp[cnt][menu] += 1
#                     cnt_temp[cnt] = max(cnt_temp[cnt], temp[cnt][menu])
#                 else:
#                     temp[cnt][menu] = 1

#     for food in course:
#         for k, v in temp[food].items():
#             # print(k, v)
#             if v >= 2 and v == cnt_temp[food]:
#                 answer.append(k)
    

#     return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"]) # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"]) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4])) # ["WX", "XY"]

