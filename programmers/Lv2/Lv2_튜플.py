from collections import Counter

def solution(s):
    answer = []
    s = s.replace('{', '').replace('}', '').split(',')
    # print(dict(Counter(s)), type(dict(Counter(s))))
    sorted_dict = sorted(dict(Counter(s)).items(), key=lambda x:x[1], reverse=True)
    # print(sorted_dict)

    for x, y in sorted_dict:
        # print(x, y)
        answer.append(int(x))
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4]) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4]) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}") == [111, 20]) # [111, 20]
print(solution("{{123}}") == [123]) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1]) # [3, 2, 4, 1]

