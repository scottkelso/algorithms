T = 'GRNWIUNQPOVDN          FEWV  R   VJSV                F                    EWW'
P = '                    '
k= len(P)-1
j= len(P)-1
c=0
while j < len(T) and k >= 0:
    print("k is " + str(k) + " and j is " + str(j))
    c = c + 1
    if T[j] == P[k]:
        j = j - 1
        k = k - 1
        print("k-- is " + str(k) + " and j-- is " + str(j))
    else:
        print("j is j + 8")
        j = j + len(P)
        print("Therefore j is " + str(j))

        k = len(P)-1
if k == -1:
    print("Match found at " + str(j+1))
else:
    print("No match")

print(str(c)+" comparisions")




T = 'GRNWIUNQPOVDN          FEWV  R   VJSV                F                    EWW'
P = '                    '
k= len(P)-1
j= len(P)-1
c=0
while j < len(T) and k >= 0:
    c = c + 1
    if T[j] == P[k]:
        j = j - 1
        k = k - 1
    else:
        j = j + len(P)
        k = len(P)-1
if k == -1:
    print("Match found at " + str(j+1))
else:
    print("No match")
