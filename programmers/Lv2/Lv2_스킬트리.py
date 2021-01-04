def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)

    for i in skill_trees:
        # print(i)
        idx = 0
        ck = True

        for j in i:
            # print(j)
            if j in skill:
                if skill[idx] == j:
                    idx += 1
                else:
                    ck = False
                    break
        if ck:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
