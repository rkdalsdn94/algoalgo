# 프로그래머스 Lv1 - 성격 유형 검사하기 - 구현, 자료 구조 문제
'''
구현, 자료 구조 문제

카카오 문제는 항상 지문이 길어서 이해하는데 시간이 좀 걸리는거 같다.
문제 이해만 잘 되면 구현은 어렵지 않다.

모든 성격 유형을 담고있는 dict을 하나 만든 뒤에
문제에 주어진 채점 방식으로 4(모르겠음) 경우만 빼고 temp 딕셔너리의 해당 성격(키)에 성격 유형 점수(값)을 더한다.
최종적으로 answer에 추가할 때 값이 같을 경우 사전 순으로 온다는 부분만 주의 한 다음
값이 더 큰 성격으로 answer에 추가하면 된다.
'''

def solution(survey, choices):
    answer = ''
    temp = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    
    for i in range(len(survey)):
        if choices[i] == 4:
            pass
        elif choices[i] == 1:
            temp[survey[i][0]] += 3
        elif choices[i] == 2:
            temp[survey[i][0]] += 2
        elif choices[i] == 3:
            temp[survey[i][0]] += 1
        elif choices[i] == 5:
            temp[survey[i][1]] += 1
        elif choices[i] == 6:
            temp[survey[i][1]] += 2
        elif choices[i] == 7:
            temp[survey[i][1]] += 3

    answer += 'R' if temp['R'] >= temp['T'] else 'T'
    answer += 'C' if temp['C'] >= temp['F'] else 'F'
    answer += 'J' if temp['J'] >= temp['M'] else 'M'
    answer += 'A' if temp['A'] >= temp['N'] else 'N'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # "RCJA"