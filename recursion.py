from math import floor


# def smaller_half(list):
#     if len(list) > 1:
#         # print("List is " + str(len(list)) + " in length.")
#         slice_size = floor(len(list) / 2) - 1
#         half = list[0:slice_size]
#         # print("Taking slice of " + str(slice_size) + " in length.")
#         return 1 + smaller_half(half)
#     else:
#         return 1


# print(smaller_half(list(range(1, 11))))


def smaller_half(n):
    print("Maximum size of smaller sublist of list of size " + str(n) + " is " + str((n - 2 + (n % 2)) / 2))


smaller_half(3)
smaller_half(4)
smaller_half(5)
smaller_half(6)
smaller_half(7)
smaller_half(8)
smaller_half(9)
smaller_half(10)
smaller_half(11)
smaller_half(12)