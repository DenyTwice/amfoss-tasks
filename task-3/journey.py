t = int(input())

def check(lst):
    if len(lst) == 3:
        print("YES")
    else:
        print("NO")
journ = []
for i in range(t):
    myKey = int(input())
    realmKey = list(map(int, input().split()))
    journ.append(myKey)
    if realmKey[myKey-1] != 0:
        journ.append(realmKey[myKey-1])
        nxtKey = realmKey[myKey-1]
        if realmKey[nxtKey-1] != 0:
            journ.append(realmKey[nxtKey-1])
    check(journ)
    

    
