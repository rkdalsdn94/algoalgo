'''
제한사항
 - 전체 학생의 수는 2명 이상 30명 이하입니다.
 - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
 - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
 - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
 - 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
  남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

위에 제한사항 중 마지막 부분 때문에 list comprehension에서 not in 조건을 만들었고,
기존엔 정렬을 안해도 통과 됐었는데, 테스트 케이스가 추가된 후에는 정렬을 안하면 통과가 안된다.
'''
def solution(n, lost, reserve):
    answer = n
    lost, reserve = sorted([i for i in lost if i not in reserve]), sorted([i for i in reserve if i not in lost])
    
    for i in reserve:
        a, b = i - 1, i + 1
        
        if a in lost:
            lost.remove(a)
        elif b in lost:
            lost.remove(b)

    return answer - len(lost)

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
print(solution(7, [2,3,4], [1,2,3,6])) # 6  # 제한사항중 제일 마지막 부분 때문에 6이 나와야 한다.
