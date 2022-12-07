t = int(input())

for i in range(t):
    numTank = int(input())
    
    zroTanks = 0
    
    tank = list(map(int,input().split()))
    
    while tank[0] == 0:
        del tank[0]
    
    last = tank.pop()
    
    if len(tank) == 0:
        print("0")
    
    for ltr in tank:
        if ltr == 0:
            zroTanks += 1

    if len(tank) >= 1:
        sum = 0
        
        for j in range(len(tank)):
            sum += tank[j]
        
        print(sum+zroTanks)