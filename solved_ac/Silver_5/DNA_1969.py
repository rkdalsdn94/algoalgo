'''
구현, 문자열, 완전 탐색

DNA(res)를 구하는 거는 각 단어 글자 마다 제일 많이 나오는 값으로 구하면 된다.
max값이 동일할 때 순서를 고민했었는데, 예제를 보니까 정렬된 기준('A', 'C', 'G', 'T') 순으로 하면 된다.
그리고 max값이 아닌 글자들을 hamming_distance에 다 더한 값으로 append하고, sum으로 출력하면 된다.
'''

n, m = map(int, input().split())
dna_list = [ list(input()) for _ in range(n) ]

# 테스트
# n, m = 5, 8
# dna_list = [['T','A','T','G','A','T','A','C'], ['T','A','A','G','C','T','A','C'],
#             ['A','A','A','G','A','T','C','C'], ['T','G','A','G','A','T','A','C'],
#             ['T','A','A','G','A','T','G','T']] # TAAGATAC \n 7
# n, m = 4, 10
# dna_list = [['A','C','G','T','A','C','G','T','A','C'], ['C','C','G','T','A','C','G','T','A','G'],
#             ['G','C','G','T','A','C','G','T','A','T'], ['T','C','G','T','A','C','G','T','A','A']] # ACGTACGTAA \n 6
# n, m = 6, 10
# dna_list = [['A','T','G','T','T','A','C','C','A','T'], ['A','A','G','T','T','A','C','G','A','T'],
#             ['A','A','C','A','A','A','G','C','A','A'], ['A','A','G','T','T','A','C','C','T','T'],
#             ['A','A','G','T','T','A','C','C','A','A'], ['T','A','C','T','T','A','C','C','A','A']] # AAGTTACCAA \n 12

res, hamming_distance = '', []

for i in range(m):
    dna_word = [0,0,0,0] # 각 순서대로 A, C, G, T

    for j in range(n):
        if dna_list[j][i] == 'A':
            dna_word[0] += 1
        elif dna_list[j][i] == 'C':
            dna_word[1] += 1
        elif dna_list[j][i] == 'G':
            dna_word[2] += 1
        elif dna_list[j][i] == 'T':
            dna_word[3] += 1
        
    idx = dna_word.index(max(dna_word))

    if idx == 0:
        res += 'A'
        hamming_distance.append(dna_word[1] + dna_word[2] + dna_word[3]) # max값을 제외한 나머지를 더한 값으로 append
    if idx == 1:
        res += 'C'
        hamming_distance.append(dna_word[0] + dna_word[2] + dna_word[3])
    if idx == 2:
        res += 'G'
        hamming_distance.append(dna_word[0] + dna_word[1] + dna_word[3])
    if idx == 3:
        res += 'T'
        hamming_distance.append(dna_word[0] + dna_word[1] + dna_word[2])

print(res)
print(sum(hamming_distance))
