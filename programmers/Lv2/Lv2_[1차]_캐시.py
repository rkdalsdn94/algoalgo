from collections import deque
def solution(cacheSize, cities):
    answer = 0
    temp = deque()
    
    for i in cities:
        i = i.lower()
        
        if i in temp:
            answer += 1
            temp.remove(i)
            temp.append(i)
        else:
            answer += 5
            if cacheSize != 0:
                if len(temp) >= cacheSize:
                    temp.popleft()
                temp.append(i)

    return answer
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 
                   'LA'])) # 50
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25