t = int(input())

for i in range(t):
    num = int(input())
    list1 = list(map(int, input().split()))
    for i in range(num):
        try:
            if list1[i+1] % list1[i] == 0:
                list1[i+1] = list1[i]
            else:
                print("NO")
                break
        except IndexError:
            if set(list1) == {list1[0]}:
                print("YES")
            else:
                print("NO")
    
