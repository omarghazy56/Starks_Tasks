n = int(input())
list = list(map(int, input().split()))
maxi = max(list)
while max(list)==maxi:
    list.remove(maxi)
print(max(list))
