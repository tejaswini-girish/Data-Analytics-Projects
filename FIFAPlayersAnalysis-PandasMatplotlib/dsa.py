a =  [2**10, 0, 1, 2, 0, 1, 2]
Q = [[3,3], [4, 4]]



sums = []
for n in Q:
    i = n[0]
    j = n[1]
    sum = 0
    if(i>j):
        i, j = n[1],n[0]
    for p in a[i:j+1]:
        sum += p
    sums.append(sum)

print(sums)

