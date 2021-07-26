def solution(s):
    answer = ""
    word_dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    word = ""

    for i in s:
        if i.isdigit():
            answer += i
        else:
            word += i
        
            if word in word_dic.keys():
                answer += word_dic[word]
                word = ""
        
    return int(answer)

print(solution("one4seveneight")) # 1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123