numP = int(input())
coords = []
ideal = 0
idealPoint = {1, 2, 3, 4}
checkr = []

def check(x1, x2, y1, y2):
    if x2 > x1 and y2 == y1:
        checkr.append(1)
    elif x2 < x1 and y2 == y1:
        checkr.append(2)
    elif x2 == x1 and y2 < y1:
        checkr.append(3)
    elif x2 == x1 and y2 > y1:
        checkr.append(4)


for i in range(numP):
    coord = list(map(int, input().split()))
    coords.append(coord)
for i in range(len(coords)):
    for j in range(len(coords)):
        check(coords[i][0], coords[j][0], coords[i][1], coords[j][1])

    checkr.sort()
    checkrSet = [*set(checkr)]

    if checkrSet == idealPoint and len(checkrSet) == 4:
        ideal += 1
        checkr = []
        checkrSet = set()
    else:
        checkr = []
        checkrSet = set()
        
print(ideal)