val = list(map(int, input().split()))
result = []

if val[0] < val[1]:
    print(-1)
    exit()
if val[0] == val[1]:
    print(val[0])
    exit()

quo = int(val[0]/2)

for i in range(quo):
    result.append(2)
if (val[0] % 2) == 1:
    result.append(1)
while (len(result) % val[1]) != 0:
    try:
        result.remove(2)
        result.append(1)
        result.append(1)
    except ValueError:
        print(-1)
        exit()

print(len(result))
