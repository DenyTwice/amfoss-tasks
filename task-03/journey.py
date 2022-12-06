t = int(input())

for i in range(t):
    myKey = int(input())
    realmKey = list(map(int, input().split()))
    journ = []
    journ.append(myKey)
    if realmKey[myKey-1] != 0:
        journ.append(realmKey[myKey-1])
        nxtKey = realmKey[myKey-1]
        if realmKey[nxtKey-1] != 0:
            journ.append(realmKey[nxtKey-1])
    if len(journ) == 3:
        print("YES")
    else:
        print("NO")
    