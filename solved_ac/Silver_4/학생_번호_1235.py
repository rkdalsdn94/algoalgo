'''
Counter를 써서 길이(len)를 비교하다가 다른 사람 풀이에 set 자료구조를 사용해서
그 풀이가 더 좋아보여 코드를 수정했다.
'''

n = int(input())
student_number_list = [input() for _ in range(n)]
# 테스트
# n = 3
# student_number_list = ['1212345', '1212356', '0033445'] # 3
res = 0

for i in range(1, len(student_number_list[0]) + 1):
    temp = set()

    for j in range(n):
        temp.add(student_number_list[j][-i:])
        
    if len(temp) == n:
        res = i
        break

print(res)
