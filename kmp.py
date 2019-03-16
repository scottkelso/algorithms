T = 'DABDAADADDABDABDAADAB'
P = 'DABDAADAB'
k=0
j=0
c=0
print("k++ is "+str(k)+" and j++ is "+str(j))
while j< len(T) and k < len(P):
    while k >= 0 and T[j] != P[k]:
        c = c + 1
        if P[0] == P[k]:
            k = -1
        else:
            k = 0
        print("next(k) is "+ str(k))
    if k>=0:
        c = c + 1
    k = k + 1
    j = j + 1
    print("k++ is "+str(k)+" and j++ is "+str(j))

print(str(c)+" comparisions")

