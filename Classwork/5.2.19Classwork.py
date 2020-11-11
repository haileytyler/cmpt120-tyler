# Hailey Tyler
# Lab on Sorting and Searching
# May 2, 2019

# Part 1:
# 3


def Ordered_binary_Search(olist, item):
    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist) // 2
        if olist[midpoint] == item:
            return True
        else:
            if item < olist[midpoint]:
                return binarySearch(olist[:midpoint], item)
            else:
                return binarySearch(olist[midpoint + 1:], item)


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

# 4


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubbleSort(nlist)
print(nlist)

# 5


def selectionSort(nlist):
    for fillslot in range(len(nlist)-1, 0, -1):
        maxpos = 0
        for location in range(1, fillslot+1):
            if nlist[location] > nlist[maxpos]:
                maxpos = location

        temp = nlist[fillslot]
        nlist[fillslot] = nlist[maxpos]
        nlist[maxpos] = temp


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
selectionSort(nlist)
print(nlist)

# 8


def mergeSort(nlist):
    print("Splitting ", nlist)
    if len(nlist) > 1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i = i+1
            else:
                nlist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j+1
            k = k+1
    print("Merging ", nlist)


nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
mergeSort(nlist)
print(nlist)

# Part 2:
# 1
fruitList = ["apples", "peaches", "pears", "grapes", "bananas"]
priceList = [0.99, 1.25, 2.35, 2.99, 0.79]


def selectionSort(nlist):
    for fillslot in range(len(nlist)-1, 0, -1):
        maxpos = 0
        for location in range(1, fillslot+1):
            if nlist[location] < nlist[maxpos]:
                maxpos = location

        temp = nlist[fillslot]
        nlist[fillslot] = nlist[maxpos]
        nlist[maxpos] = temp


selectionSort(priceList)
print(priceList)


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i] < nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


bubbleSort(priceList)
print(priceList)

#  2


def selectionSort(nlist):
    for fillslot in range(len(nlist)-1, 0, -1):
        maxpos = 0
        for location in range(1, fillslot+1):
            if nlist[location] > nlist[maxpos]:
                maxpos = location

        temp = nlist[fillslot]
        nlist[fillslot] = nlist[maxpos]
        nlist[maxpos] = temp


selectionSort(fruitList)
print(fruitList)


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


bubbleSort(fruitList)
print(fruitList)


