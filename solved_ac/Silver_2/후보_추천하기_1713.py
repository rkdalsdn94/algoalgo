'''
구현, 시뮬레이션 문제

문제 링크 https://www.acmicpc.net/problem/1713 - 후보 추천하기

주어진 규칙대로 풀면 된다.
1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다.
   이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
5. 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

위 규칙을 잘 기억하면서 풀면 된다.
'''

# n = int(input())
# total_student_cnt = int(input())
# recommended_student_list = list(map(int, input().split()))

# 테스트
n = 3
total_student_cnt = 9
recommended_student_list = [2, 1, 4, 3, 5, 6, 2, 7, 2] # 2 6 7

photo = dict()

for i in range(total_student_cnt):
    if recommended_student_list[i] in photo:
        photo[recommended_student_list[i]][0] += 1
    else:
        if len(photo) < n:
            photo[recommended_student_list[i]] = [1, i]
        else:
            del_list = sorted(photo.items(), key=lambda x: (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[recommended_student_list[i]] = [1, i]

res = list(sorted(photo.keys()))

print(*res)
