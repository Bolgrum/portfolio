# Merge Sort and Quicksort Comparison MergeSortAndQuicksortComparison.py
# Version:                            v1.2.2.1
# Developed by:                       Anthony Braden from 04/13/2021-04/13/2021

import random
import sys
import time
sys.setrecursionlimit(4000)

i = sys.argv[1]
number = int(sys.argv[2])

def mergeSort(arrayMergeSort):
    if len(arrayMergeSort) > 1:
        mid = len(arrayMergeSort) // 2
        left = arrayMergeSort[:mid]
        right = arrayMergeSort[mid:]

        mergeSort(left)
        mergeSort(right)

        iteratorLower = 0
        iteratorUpper = 0
        iteratorMain = 0
        
        while iteratorLower < len(left) and iteratorUpper < len(right):
            if left[iteratorLower] < right[iteratorUpper]:
                
              arrayMergeSort[iteratorMain] = left[iteratorLower]
              iteratorLower += 1
            else:
                arrayMergeSort[iteratorMain] = right[iteratorUpper]
                iteratorUpper += 1
            iteratorMain += 1

        while iteratorLower < len(left):
            arrayMergeSort[iteratorMain] = left[iteratorLower]
            iteratorLower += 1
            iteratorMain += 1

        while iteratorUpper < len(right):
            arrayMergeSort[iteratorMain] = right[iteratorUpper]
            iteratorUpper += 1
            iteratorMain += 1
            
def partition(arrayQuickSort, low, high):
    index = (low-1)
    pivot = arrayQuickSort[high]
  
    for arrayElement in range(low, high):
        if arrayQuickSort[arrayElement] <= pivot:
            index += 1
            arrayQuickSort[index] = arrayQuickSort[arrayElement]
            arrayQuickSort[arrayElement] = arrayQuickSort[index]
            
    arrayQuickSort[index+1] = arrayQuickSort[high]
    arrayQuickSort[high] = arrayQuickSort[index+1]
    return (index+1)  

def quickSort(arrayQuickSort, low, high):
    if len(arrayQuickSort) == 1:
        return arrayQuickSort
    if low < high:
        pi = partition(arrayQuickSort, low, high)
        quickSort(arrayQuickSort, low, pi-1)
        quickSort(arrayQuickSort, pi+1, high)
        
def makeArrayListOfRandomNumbers(array, smallNumber):
    for x in range(smallNumber):
        a = 1
        b = 1000
        c = random.randint(a, b)
        array.append(c)
        
runNumber = 1
for x in range(1000):
    arrayMergeSort = []
    arrayQuickSort = []
    
    if (number < 100):
        for y in range(int(number / 10)):
            array = []
            smallNumber = int(number / 5)
            makeArrayListOfRandomNumbers(array, smallNumber)
        
            arrayMergeSort = arrayMergeSort + array
            arrayQuickSort = arrayQuickSort + array 
    else:
        for y in range(int(number / 100)):
            array = []
            smallNumber = int(number / 5)
            makeArrayListOfRandomNumbers(array, number)
        
            arrayMergeSort = arrayMergeSort + array
            arrayQuickSort = arrayQuickSort + array 

    start_timeMerge = time.time()
    mergeSort(arrayMergeSort)
    end_timeMerge = time.time()
    timeMerge = format(round((end_timeMerge - start_timeMerge), 24), '.24f')
    
    arrayLengthQuickSort = len(arrayQuickSort)
    start_timeQuick = time.time()
    quickSort(arrayQuickSort, 0, arrayLengthQuickSort-1)
    end_timeQuick = time.time()
    timeQuick = format(round((end_timeQuick - start_timeQuick), 24), '.24f')

    outFileName = 'MergeSortAndQuicksortComparison' + '_Results_' + str(i) + '.txt'
    outputString = str(runNumber) + ',' + str(runNumber) + ',' + str(timeMerge) + ',' + str(timeQuick) 
    with open(outFileName, 'a') as f:
        print(outputString, file=f)
    runNumber += 1