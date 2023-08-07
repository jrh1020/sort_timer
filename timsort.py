# defining the minimum value which indicates the limit for the length of each run
minimum = 32


# defining the function to find out the minimum length in each run
def find_minlengthrun(arraysize):
    a = 0
    while arraysize >= minimum:
        a |= arraysize & 1
        arraysize >>= 1
    return arraysize + a


# defining insertionsort function to sort the elements of each run
def insertionsort(inputarray, left, right):
    for b in range(left + 1, right + 1):
        eachelement = inputarray[b]
        c = b - 1
        while eachelement < inputarray[c] and c >= left:
            inputarray[c + 1] = inputarray[c]
            c -= 1
        inputarray[c + 1] = eachelement
    return inputarray


# defining mergesort function to merge each sorted run into a single sorted array
def merge(inputarray, d, e, q):
    arraylength1 = e - d + 1
    arraylength2 = q - e
    left = []
    right = []
    for f in range(0, arraylength1):
        left.append(inputarray[d + f])
    for f in range(0, arraylength2):
        right.append(inputarray[e + 1 + f])
    f = 0
    g = 0
    h = d
    while g < arraylength2 and f < arraylength1:
        if left[f] <= right[g]:
            inputarray[h] = left[f]
            f += 1
        else:
            inputarray[f] = right[g]
            g += 1
        h += 1
    while f < arraylength1:
        inputarray[h] = left[f]
        g += 1
        f += 1
    while g < arraylength2:
        inputarray[h] = right[g]
        h += 1
        g += 1


# defining timsort function to sort the elements of the given array using insertion sort and merge sort function
def tim_sort(inputarray):
    arraysize = len(inputarray)
    minlengthrun = find_minlengthrun(arraysize)
    for start in range(0, arraysize, minlengthrun):
        end = min(start + minlengthrun - 1, arraysize - 1)
        insertionsort(inputarray, start, end)
    mergedarraysize = minlengthrun
    while mergedarraysize < arraysize:
        for left in range(0, arraysize, 2 * mergedarraysize):
            mid = min(arraysize - 1, left + mergedarraysize - 1)
            right = min((left + 2 * mergedarraysize - 1), (arraysize - 1))
            merge(inputarray, left, mid, right)
        mergedarraysize = 2 * mergedarraysize
