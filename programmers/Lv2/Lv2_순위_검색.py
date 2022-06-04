'''
구현, 자료 구조 문제

자료 구조를 잘 활용해서 구현하면 되는 문제이다.
근데, 시간도 오래 걸리고 풀이도 잘 생각이 안나.. 여러 검색해서 아래 링크 통해서 이해할 수 있었다.

https://youtu.be/b_LRHAB1Xh4?list=PL6YHvWRMtz7CUn7iYH5qMvbDVGk1NElQS&t=334 여기 링크에서 비트 연산자를 공부하면 더 좋다.
https://www.youtube.com/watch?v=izxzh0rQxSI 해당 링크에서 문제 풀이를 확인해보면 된다.
'''

from bisect import bisect_left as bi_left

def solution(info, query):
    dic = {
        '-': 0, 'cpp': 1, 'java': 2, 'python': 3,
        'frontend': 1, 'backend': 2,
        'junior': 1, 'senior': 2,
        'chicken': 1, 'pizza': 2
    }
    temp = [ [] for _ in range(4 * 3 * 3 * 3) ]
    answer = []
    
    for s in info:
        word = s.split()
        # print(word)
        arr = (dic[word[0]] * 3 * 3 * 3,
              dic[word[1]] * 3 * 3,
              dic[word[2]] * 3,
              dic[word[3]])
        score = int(word[4])
        
        for i in range(16):
            idx = 0
            
            for j in range(4):
                if i & ( 1 << j):
                    idx += arr[j]
            temp[idx].append(score)
    
    for i in range(4 * 3 * 3 * 3):
        temp[i].sort()
    
    for s in query:
        word = s.split()
        # print(word)
        idx = dic[word[0]] * 3 * 3 * 3 + dic[word[2]] * 3 * 3 + dic[word[4]] * 3 + dic[word[6]]
        score = int(word[7])
        answer.append(len(temp[idx]) - bi_left(temp[idx], score))
    
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query)) # [1,1,1,1,2,4]
