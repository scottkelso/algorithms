def match(P, T):
    i = 0
    j = 0
    k = 0
    while j < len(T) and k < len(P):
        if T[j] == P[k]:
            j = j + 1
            k = k + 1
        else:
            i = i + 1
            j = i
            k = 0
    if k >= len(P):
        print("Match found at", i)
    else:
        print("No match")


text = 'ABBIBAARABIA'
pattern = 'ARABIA'
match(pattern, text)
