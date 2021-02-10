def triangle_snail(x, y, i):
        if i % 3 == 0:
            x += 1
        elif i % 3 == 1:
            y += 1
        else:
            x -= 1
            y -= 1
        
        return x, y

def solution(n):
    answer = []
    temp = [[0]*i for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    # print(temp)

    for i in range(n):
        for _ in range(i, n):
            x, y = triangle_snail(x, y, i)
            temp[x][y] = num
            num += 1
    
    for i in temp:
        answer.extend(i)

    return answer
print(solution(4) == [1,2,9,3,10,8,4,5,6,7]) # [1,2,9,3,10,8,4,5,6,7]
print(solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]