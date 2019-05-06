import numpy as np


def quicksort(first, last):
    if first < last:
        splitpoint = split(first, last)
        quicksort(first, splitpoint-1)
        quicksort(splitpoint+1, last)


def quicksort_with_stacking_right_sublist(first, last):
    stack = []
    stack.append((first, last))
    while len(stack) > 0:
        (first, last) = stack.pop()
        # print("stack " + str(len(stack)) + " big")
        while first < last:
            splitpoint = split(first, last)
            stack.append((splitpoint+1, last))
            last = splitpoint-1
            # print("stack " + str(len(stack)) + " big")


def quicksort_with_stacking_left_sublist(first, last):
    stack = []
    stack.append((first, last))
    while len(stack) > 0:
        (first, last) = stack.pop()
        # print("stack " + str(len(stack)) + " big")
        while first < last:
            splitpoint = split(first, last)
            stack.append((first, splitpoint-1))
            first = splitpoint+1
            # print("stack " + str(len(stack)) + " big")


def quicksort_with_stacking_largest_sublist(first, last):
    stack = []
    stack.append((first, last))
    stack_sizes = []
    while len(stack) > 0:
        stack_sizes.append(len(stack))
        (first, last) = stack.pop()
        stack_sizes.append(len(stack))
        while first < last:
            splitpoint = split(first, last)
            if splitpoint - first >= last - splitpoint:
                stack.append((first, splitpoint-1))
                first = splitpoint+1
            else:
                stack.append((splitpoint+1, last))
                last = splitpoint-1
            stack_sizes.append(len(stack))
    return max(stack_sizes)


def split(first, last):
    x = l[first]
    splitpoint = first

    # Check every other value other than first
    for unknown in range(first+1, last+1):
        if l[unknown] < x:
            splitpoint = splitpoint + 1
            interchange(splitpoint, unknown)
            # print(l)
        # else:
        #     print(l)

    interchange(first, splitpoint)
    # print(l)
    return splitpoint


def interchange(index1, index2):
    temp = l[index1]
    l[index1] = l[index2]
    l[index2] = temp


def quicksorter(list):
    global l
    l = list
    max = quicksort_with_stacking_largest_sublist(0, len(list)-1)
    return max


# quicksorter([2, 5, 9, 1, 3, 10, 6, 19, 7])
# quicksorter([9, 8, 10, 7, 11, 6, 12, 5, 13])
# quicksorter([20, 19, 18, 17, 16, 15, 14, 13, 12])
# quicksorter([1, 2, 3, 4, 5, 6, 7, 8, 9])
# quicksorter([2, 5, 9, 1, 3])
# quicksorter([8, 7, 2, 5, 9])
# quicksorter([6, 8, 5, 10, 2])
# quicksorter([3, 2, 1])
# quicksorter([3, 2])
# quicksorter([1, 2])

maxs = []
for i in range(100):
    # print(type(list(permutation)))
    maxs.append(quicksorter(list(np.random.permutation(20))))

print(max(maxs))
