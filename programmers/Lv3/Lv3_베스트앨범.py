def solution(genres, plays):
    answer = []
    genre = {}
    for i, j in zip(genres, plays):
        if i in genre:
            genre[i] += j
        else:
            genre[i] = j

    genre = [i for i, j in sorted(
        genre.items(), key=lambda x: x[1], reverse=True)]

    dic = {}
    for i, j in enumerate(zip(genres, plays)):
        if j[0] in dic:
            dic[j[0]].append([j[1], i])
        else:
            dic[j[0]] = list()
            dic[j[0]].append([j[1], i])

    temp = []
    for i in genre:
        temp = sorted(dic[i], key=lambda x: x[0], reverse=True)
        if len(temp) > 1:
            answer.append(temp[0][1])
            answer.append(temp[1][1])
        else:
            answer.append(temp[0][1])

    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
               [500, 600, 150, 800, 2500]))  # [4,1,3,0]
# def solution(genres, plays):
#     answer = []

#     genre = {}
#     dic = {}
#     for i, (x, y) in enumerate(zip(genres, plays)):
#         if i in genre:
#             genre[x] += y
#         else:
#             genre[x] = y
#         if x in dic:
#             dic[x].append([y, i])
#         else:
#             dic[x] = []
#             dic[x].append([y, i])

#     genre = [i for i, j in sorted(
#         genre.items(), key=lambda x: x[1], reverse=True)]
#     temp = []
#     for i in genre:
#         temp = sorted(dic[i], key=lambda x: x[0], reverse=True)
#         if len(temp) > 1:
#             answer.append(temp[0][1])
#             answer.append(temp[1][1])
#         else:
#             answer.append(temp[0][1])

#     return answer


# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
#                [500, 600, 150, 800, 2500]))  # [4,1,3,0]
