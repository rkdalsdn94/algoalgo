# 백준 - 실버5 - 출입 기록 - 27111 - 구현, 에드 훅, 시뮬레이션 문제
'''
구현, 에드 훅, 시뮬레이션 문제

단순하게 생각나는대로 구현했다가 시간 초과를 받았다. 시간 초과 코드는 파일 제일 아래에 있다.
에드 훅 문제는 대부분 약간의 꼼수(?)가 있다. 이 문제에선 n의 최대 범위만큼 list로 만든 후 해당 인덱스의 값이 있는지 없는지로 구할 수 있다.
단, 부대에서 입장 기록은 있는데, 나오는 기록이 없을 수 있으므로 sum 을 통해 나가지 못한 인원들도 추개햐야 한다.

다른 사람의 풀이에선 if ck[i] == b: 이런 방식으로 푼 사람들이 많은데 해당 코드가 더 읽기 편한거 같다.
'''

n = int(input())
visit_history = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 8
# visit_history = [ [1, 1], [2, 1], [1, 1], [4, 1], [3, 0], [5, 1], [4, 0], [1, 0] ] # 4
# n = 4
# visit_history = [ [100, 1], [345, 1], [345, 0], [100, 0] ] # 0

ck = [0] * 200_001
res = 0

for i, j in visit_history:
    if j == 1:
        if ck[i] == 0:
            ck[i] = 1
        else:
            res += 1
    elif j == 0:
        if ck[i] == 1:
            ck[i] = 0
        else:
            res += 1
res += sum(ck)
print(res)

'''
시간 초과 코드

n = int(input())
visit_history = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 8
# visit_history = [ [1, 1], [2, 1], [1, 1], [4, 1], [3, 0], [5, 1], [4, 0], [1, 0] ] # 4
# n = 4
# visit_history = [ [100, 1], [345, 1], [345, 0], [100, 0] ] # 0

temp = []
res = 0

for i, j in visit_history:
    if j == 1 and i not in temp:
        temp.append(i)
    elif j == 0 and i in temp:
        temp.remove(i)
    else:
        res += 1

res += len(temp)
print(res)
'''
