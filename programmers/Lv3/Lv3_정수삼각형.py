'''
dp 문제

이 전에 백준에서 아예 똑같은 문제를 풀었었는데,
그때의 나와 지금의 내가 코드 짜는게 조금 바껴서 지금 푼 방식이랑 비교하면 먼가 재밌는거 같다.

백준: 정수 삼각형  1932
경로: Silver_1/정수_삼각형_1932.py 
위에 파일에서 설명을 보면 된다

j == 0 삼각형의 제일 왼쪽
j == i 삼각형의 제일 오른쪽
else 삼각형의 가운데 부분
'''

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	)) # 30