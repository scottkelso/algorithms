def kmpmatch(P, T):
    k = 0
    j = 0
    while j < len(T) and k < len(P):
        while k >= 0 and T[j] != P[k]:
            if P[0] == P[k]:
                k = -1
            else:
                k = 0
        k = k + 1
        j = j + 1


next = [10, 9, 8, 7, 4, 1]
text = 'DABDAADADDABDABDAADAB'
pattern = 'DABDAADAB'
kmpmatch(pattern, text)



# T = 'DABDAADADDABDABDAADAB'
# P = 'DABDAADAB'
# k=0
# j=0
# c=0
# print("k++ is "+str(k)+" and j++ is "+str(j))
# while j< len(T) and k < len(P):
#     while k >= 0 and T[j] != P[k]:
#         c = c + 1
#         if P[0] == P[k]:
#             k = -1
#         else:
#             k = 0
#         print("next(k) is "+ str(k))
#     if k>=0:
#         c = c + 1
#     k = k + 1
#     j = j + 1
#     print("k++ is "+str(k)+" and j++ is "+str(j))
#
# print(str(c)+" comparisions")
