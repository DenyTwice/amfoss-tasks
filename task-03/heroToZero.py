t = int(input())

for i in range(t):
    numHero = int(input())
    lvls = list(map(int,input().split()))
    lvls.sort()
    lvlSet = set(lvls)
    zeroCnt = 0
    for i in range(numHero):
        if lvls[i] == 0:
            zeroCnt += 1
    if len(lvls) == len(lvlSet):
        if zeroCnt == 0:
            print(len(lvls) + 1)
        else:
            print(len(lvls) - zeroCnt)
    else:
        if zeroCnt == 0:
            print(len(lvls))
        else:
            print(len(lvls) - zeroCnt)