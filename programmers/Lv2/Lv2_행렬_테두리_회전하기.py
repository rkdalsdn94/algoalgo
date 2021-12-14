def solution(rows, columns, queries):
    answer = []
    matrix = [ [i*columns+j+1 for j in range(columns)] for i in range(rows) ]
    
    if len(queries) != 1:
        for x1, y1, x2, y2 in queries:
            x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
            standard = matrix[x1][y1]
            minimum = standard
            
            for i in range(x1, x2):
                temp = matrix[i+1][y1]
                matrix[i][y1] = temp
                minimum = min(minimum, temp)
                
            for i in range(y1, y2):
                temp = matrix[x2][i+1]
                matrix[x2][i] = temp
                minimum = min(minimum, temp)
            
            for i in range(x2, x1, -1):
                temp = matrix[i-1][y2]
                matrix[i][y2] = temp
                minimum = min(minimum, temp)
                
            for i in range(y2, y1, -1):
                temp = matrix[x1][i-1]
                matrix[x1][i] = temp
                minimum = min(minimum, temp)
            
            matrix[x1][y1+1] = standard
            answer.append(minimum)
    else:
        answer.append(matrix[queries[0][0]-1][queries[0][1]]-1)
        
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]])) # [1]