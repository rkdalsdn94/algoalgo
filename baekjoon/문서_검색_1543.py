word = input()
search = input()

# word = 'ababababa'
# search = 'aba'

cnt = 0
temp = 0

while len(word) - temp >= len(search):
    if word[temp:temp+len(search)] == search:
        cnt += 1
        temp += len(search)
    else:
        temp += 1

print(cnt)
