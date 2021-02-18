def solution(record):
    answer = []
    
    temp = dict()
    msg = {
        'Enter':'님이 들어왔습니다.',
        'Leave':'님이 나갔습니다.'
    }
    
    for i in record:
        i = i.split()
        if len(i) == 3 :
            temp[i[1]] = i[2]
    for i in record:
        i = i.split()
        if i[0] != 'Change':
            answer.append(temp[i[1]] + msg[i[0]])
    
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]