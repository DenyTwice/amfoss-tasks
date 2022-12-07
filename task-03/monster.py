t = int(input())

for i in range(t):
    num = int(input())
    monsters = list(map(int, input().split()))
    for i in range(num):
        try:
            if monsters[i+1] % monsters[i] == 0:
                monsters[i+1] = monsters[i]
            else:
                print("NO")
                break
        except IndexError:
            if set(monsters) == {monsters[0]}:
                print("YES")
            else:
                print("NO")
    
