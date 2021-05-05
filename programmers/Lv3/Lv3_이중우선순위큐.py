# 프로그래머스 이중우선순위큐
'''
    I 숫자	 큐에 주어진 숫자를 삽입합니다.
    D 1	    큐에서 최댓값을 삭제합니다.
    D -1	큐에서 최솟값을 삭제합니다.
'''
# 프로그래머스 이중우선순위큐
def solution(operations):
    answer = []

    for i in operations:
        i = i.split()

        if i[0] == 'I':
            answer.append(int(i[1]))
        else:
            if not answer:
                pass
            elif i[1] == '1':
                answer.pop()
            else:
                answer.pop(0)
        
        answer.sort()
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]

print(solution(["I 16","D 1"]))               # [0, 0]
print(solution(["I 7","I 5","I -5","D -1"]))  # [7, 5]

