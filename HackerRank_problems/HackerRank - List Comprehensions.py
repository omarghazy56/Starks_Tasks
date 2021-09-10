list = []
x = int(input())
y = int(input())
z = int(input())
n = int(input())

for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if((a+b+c) !=n):
                abc = [a,b,c]
                list.append(abc)
print(list)
