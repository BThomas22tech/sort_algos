import math


def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)
# cList = [5,34,6,3,5,1]
# bubbleSort(cList)


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


cList = [10, 3, 4, 6, 1]
selectionSort(cList)


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)


cList = [3, 45, 6, 77, 8, 1]
insertionSort(cList)

# Binary search


def search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low)

   # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

    # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

    # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1
print(search([5,3,6,2],2))