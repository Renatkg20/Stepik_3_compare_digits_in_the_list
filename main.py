# put your python code here
l = []
l1 = []
l2 = []
n = 0
user = input("Pls inpute the numbers for compare")
for a in user.split(" "):
    l.append(int(a))

print(l)
for a in range(len(l)):
    try:
        if l[a] < l[a + 1]:
            n +=1
        else:
            pass
    except IndexError:
         pass


print(n)