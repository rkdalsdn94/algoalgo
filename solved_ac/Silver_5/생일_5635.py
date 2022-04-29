'''
구현, 정렬 문제

이름 말고 나머지 부분을 int형으로 바꾼 다음 정렬을 잘 하면 된다.
lambda를 잘 활용하면 훨씬 간편하게 코드를 짤 수 있다. (아래 코드는 연, 월, 일 순으로 차례대로 정렬을 진행한다.)
'''

n = int(input())
student_list = sorted([ list(input().split(' ')) for _ in range(n) ], key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

# 테스트
# n = 5
# student_list = sorted([
#     ['Mickey', '1', '10', '1991'], ['Alice', '30', '12', '1990'],
#     ['Tom', '15', '8', '1993'], ['Jerry', '18', '9', '1990'],
#     ['Garfield', '20', '9', '1990']
# ], key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(student_list[-1][0], student_list[0][0], sep='\n')
