val = list(map(int, input().split()))
count = 0

if val[1] == val[0]:
    print(0)
    exit()

elif val[1] < val[0]:
    print(-1)
    exit()

quo = val[1]/val[0]

while quo % 2 == 0:
    quo /= 2
    count += 1
while quo % 3 == 0:
    quo /= 3
    count += 1
    
if quo == 1:
    print(count)
else:
    print(-1)