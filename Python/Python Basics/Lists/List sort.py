sa = [0,100,1,200,33]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[i] < a[j]:
            a[i],a[j] = a[j],a[i]
print(a)