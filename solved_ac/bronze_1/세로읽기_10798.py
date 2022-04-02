# word = [ input() for _ in range(5) ]

# 테스트
word = ['ABCDE', 'abcde', '01234', 'FGHIJ', 'fghij'] # Aa0FfBb1GgCc2HhDd3IiEe4Jj
word = ['AABCDD', 'afzz', '09121', 'a8EWg6', 'P5h3kx'] # Aa0aPAf985Bz1EhCz2W3D1gkD6x

for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i], end='')
