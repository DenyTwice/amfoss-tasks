inpt = list(map(int, input().split()))

lang = {}

for i in range(inpt[1]):
    pair = input().split()
    lang[pair[0]] = pair[1]

spell = input().split()

rslt = []
for word in spell:
    if len(word) > len(lang[word]):
        rslt.append(lang[word])
    else:
        rslt.append(word)
print(rslt) 