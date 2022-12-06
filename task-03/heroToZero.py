t = int(input())
for i in range(t):
    numHero = int(input())
    heroLvl = list(map(int,input().split()))
    heroLvl.sort()
    lvlSet = len(set(heroLvl))
    zeroCnt = 0
    for i in range(len(heroLvl)):
        if heroLvl[i] == 0:
            zeroCnt += 1
    if len(heroLvl) == lvlSet:
        if zeroCnt == 0:
            print(len(heroLvl) + 1)
        else:
            print(len(heroLvl) - zeroCnt)
    else:
        if zeroCnt == 0:
            print(len(heroLvl))
        else:
            print(len(heroLvl) - zeroCnt)