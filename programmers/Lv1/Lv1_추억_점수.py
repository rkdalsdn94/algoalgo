# 프로그래머스 - Lv1 - 추억 점수 - 자료 구조(해시) 문제
'''
자료 구조(해시) 문제

[핵심 아이디어]
    - 이름과 그리움 점수를 연결하는 딕셔너리(해시 테이블)를 생성하여 빠른 조회가 가능
    - 각 사진에 등장하는 인물들의 그리움 점수를 딕셔너리에서 조회하여 합산
    - 사진에 등장하는 인물이 그리움 목록에 없는 경우는 점수에 포함하지 않음

[풀이 과정]
    1. name과 yearning 배열을 zip 함수로 결합하여 이름-점수 딕셔너리 생성
    2. 각 사진(photo의 각 원소)을 순회하면서:
        2.1. 사진 속 인물들의 그리움 점수 합계를 계산
        2.2. 인물이 딕셔너리에 존재하는 경우에만 점수를 더하기
    3. 각 사진의 점수를 결과 배열에 추가
    4. 모든 사진의 점수가 담긴 배열을 반환
'''

def solution(name, yearning, photo):
    answer = []
    name_dic = dict()

    for i, j in zip(name, yearning):
        name_dic[i] = j

    for i in photo:
        score = 0

        for j in i:
            if j in name_dic:
                score += name_dic[j]

        answer.append(score)

    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
res = [19, 15, 6]
print(solution(name, yearning, photo) == res)

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
res = [67, 0, 55]
print(solution(name, yearning, photo) == res)

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]
res = [5, 15, 0]
print(solution(name, yearning, photo) == res)
