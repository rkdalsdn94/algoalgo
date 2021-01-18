def solution(n, words):
    answer = []
    word = words[0][0]
    temp = []

    for i in range(len(words)):
        # print(words[i])
        if words[i][0] != word[-1]:
            answer.append((i % n)+1)
            answer.append((i//n)+1)
            break
        else:
            if words[i] in temp:
                answer.append((i % n)+1)
                answer.append((i//n)+1)
                break
            else:
                temp.append(words[i])
                word = words[i]
    if answer:
        return answer
    else:
        return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
                   "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
                   "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
