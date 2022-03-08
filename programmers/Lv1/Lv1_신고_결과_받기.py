'''
요즘 프로그래머스 문제를 잘 안풀서 그런지 처음에 뭔가 되게 낯설었다.
그래서 그런지 Lv1 문제인데 생각보다 시간도 걸리고 시간초과가 나와서 헤매기도 했다.
여기 올리는 최종 코드는 다른 사람이 푼 코드를 참고하여 다시 수정한 코드인데,
기존 내 코드보다 시간도 빠르고, 이해하기도 쉬워서 이 코드로 이해한 후에 수정했다.
'''

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    temp = { i: 0 for i in id_list }
    
    for i in report:
        a, b = i.split()
        temp[b] += 1
        
    for i in report:
        a, b = i.split()
        
        if temp[b] >= k:
            answer[id_list.index(a)] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) # [2,1,1,0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) # [0,0]
