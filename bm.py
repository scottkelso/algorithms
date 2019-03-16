T = 'ABBIBAARABIA'
P = 'ARABIA'
charJump = {'A': 0, 'I': 1, 'B': 2, 'R': 4}
matchJump = [10, 9, 8, 7, 4, 1]
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
        if T[j] in charJump:
            print("j is j + max(" + str(charJump[T[j]]) + ", " + str(matchJump[k])+")")
            j = j + max(charJump[T[j]], matchJump[k])
        else:
            print("j is j + max(6, " + str(matchJump[k])+")")
            j = j + max(6, matchJump[k])
        print("Therefore j is " + str(j))

        k = len(P)-1
if k == -1:
    print("Match found at " + str(j+1))
else:
    print("No match")

print(str(c)+" comparisions")

