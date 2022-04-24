'''
구현, 정렬 문제이다

입력으로 들어오는 조건중에 reverse = True 조건을 줘서 내림차순으로 만들고, 
1등과 2등 참가국이 같으면 4번째 출력, 참가국이 다르면 3번째 출력하면 된다.
'''

n = int(input())
student = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: x[2], reverse=True)

# 테스트
# n = 9 # 1 1 \n 1 2 \n 3 4
# student = sorted([[1, 1, 230], [1, 2, 210], [1, 3, 205],
#             [2, 1, 100], [2, 2, 150], [3, 1, 175], [3, 2, 190],
#             [3, 3, 180], [3, 4, 195]], key=lambda x: x[2], reverse=True)
temp = 0

if student[0][0] == student[1][0]:
    temp = 1

print(*student[0][:2])
print(*student[1][:2])

for i in range(2, n):
    if temp == 0:
        print(*student[i][:2])
        break
    else:
        if student[1][0] != student[i][0]:
            print(*student[i][:2])
            break
