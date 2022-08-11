'''
단수 구현 문제

버블 정렬을 구하면 되는 문제이다.
'''

piece = list(map(int, input().split()))

# 테스트
# piece = [2,1,5,3,4] # 1 2 5 3 4 \n 1 2 3 5 4 \n 1 2 3 4 5
# piece = [2,3,4,5,1] # 2 3 4 1 5 \n 2 3 1 4 5 \n 2 1 3 4 5 \n 1 2 3 4 5

temp = sorted(piece)

while temp != piece:
    for i in range(len(piece) - 1):
        if piece[i] > piece[i + 1]:
            piece[i], piece[i + 1] = piece[i + 1],piece[i]
            print(*piece)
