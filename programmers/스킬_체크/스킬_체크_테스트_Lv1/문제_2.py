'''
실패율이랑 똑같은 문제이다
기존 실패율이랑은 다르게 풀렸던거 같다.
이전에 문제 풀어 봤던거를 다시 풀어보는 연습도 해야 될 거같다.
'''
def solution(N, stages):
    answer = []
    temp = len(stages)
    temp_dic = {}

    for i in range(1, N+1):
        if temp != 0:
            player = stages.count(i)
            temp_dic[i] = player / temp
            temp -= player
        else: temp_dic[i] = 0

    for i in sorted(temp_dic, key=lambda x: temp_dic[x], reverse=True):
        answer.append(i)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3