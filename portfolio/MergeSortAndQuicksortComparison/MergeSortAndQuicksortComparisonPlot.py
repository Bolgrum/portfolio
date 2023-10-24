# Plot OSG data                                         MergeSortAndQuicksortComparisonPlot.py
# Version                                               v3.1.1
# Completed by:                                         Anthony Braden on 07/28/2021

# Modify the Algoriths problem statement from 'Divide and Conquer Algoriths.txt'
# for optimization on the Open Science Grid. The work should document the 
# following:
# 1. Average wall-clock time.
# 2. Minimum wall-clock time.
# 3. How many times the expected results (Quicksort < Mergesort) fails to 
# appear.
# 4. Keep the data pairs and sort for minimum time.
# 5. Do 1-4 for multiple array sizes.

import csv
import matplotlib.pyplot as plt
import numpy as np

allAverageMergeSortTimes = []
allMinimalMergeSortTimes = []

allAverageQuicksortTimes = []
allMinimalQuicksortTimes = []

class mergeSort():
    
    def __init__(self):
        self.mergeSortTimes = []
        
    def collectMergeSortTimes(self, sequencialResultsFileName):
        with open(sequencialResultsFileName) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                self.mergeSortTimes.append(row[2])
            return self.mergeSortTimes
        
    def findAverageMergeSortWallClockTime(self):
        mergeSortTimesAverage = sum(map(float, self.mergeSortTimes)) / len(self.mergeSortTimes)
        allAverageMergeSortTimes.append(mergeSortTimesAverage)
        return mergeSortTimesAverage
        
    def findMinimalMergeSortWallClockTime(self):
        sortedMergeSortTimes = sorted(self.mergeSortTimes)
        minimalMergeSortTime = sortedMergeSortTimes[0]
        allMinimalMergeSortTimes.append(minimalMergeSortTime)
        return minimalMergeSortTime
        
class quicksort():
    def __init__(self):
        self.quicksortTimes = []
        
    def collectQuicksortTimes(self, sequencialResultsFileName):
        with open(sequencialResultsFileName) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                self.quicksortTimes.append(row[3])
            return self.quicksortTimes
        
    def findAverageQuicksortWallClockTime(self):
        quicksortTimesAverage = sum(map(float, self.quicksortTimes)) / len(self.quicksortTimes)
        allAverageQuicksortTimes.append(quicksortTimesAverage)
        return quicksortTimesAverage
        
    def findMinimalQuicksortWallClockTime(self):
        sortedQuicksortTimes = sorted(self.quicksortTimes)
        minimalQuicksortTime = sortedQuicksortTimes[0]
        allMinimalQuicksortTimes.append(minimalQuicksortTime)
        return minimalQuicksortTime
        
class columnStack():
    def __init__(self):
        self.stackOfTimes = []
        
    def createStackOfSortTimes(self, mergeSortTimes, quicksortTimes):
        self.stackOfTimes = np.column_stack((mergeSortTimes, quicksortTimes))
        return self.stackOfTimes
        
    def findNumberOfResultsThatFailExpectation(self):
        count = 0
        for list in self.stackOfTimes:
            if list[0] < list[1]:
                count += 1
        return count
    
    def findMinimumTimeInPairsForMergeSort(self):
        minimumMergeSortTime = []
        sortedStackOfTimesForMergeSort = sorted(self.stackOfTimes, key=lambda x:x[0])
        minimumMergeSortTime.append(sortedStackOfTimesForMergeSort[0])
        return minimumMergeSortTime
        
    def findMinimumTimeInPairsForQuicksort(self):
        minimumQuicksortTime = []
        sortedStackOfTimesForQuicksort = sorted(self.stackOfTimes, key=lambda x:x[1])
        minimumQuicksortTime.append(sortedStackOfTimesForQuicksort[1])
        return minimumQuicksortTime
        
class printResults():
    def __init__(self):
        self.outFileName = 'DivideAndConquerSortResults.txt'
        
    def printHeader(self):
        outputString = 'Results from', sequencialResultsFileName
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)  
             
    def printAverageMergeSortWallClockTime(self, mergeSortTimesAverage):
        outputString = 'Merge Sort average time is:', str(mergeSortTimesAverage)
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
            
    def printAverageQuicksortWllClockTime(self, quicksortTimesAverage):
        outputString = 'Quicksort average time is:', str(quicksortTimesAverage)
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
            
    def printMinimalMergeSortWallClockTime(self, minimalMergeSortTime):
        outputString = 'Minimal Merge Sort time is:', str(minimalMergeSortTime)
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
            
    def printMinimalQuickSortWallClockTime(self, minimalQuicksortTime):
        outputString = 'Minimal Quicksort time is:', str(minimalQuicksortTime)
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
            
    def printNumberOfResultsThatFailExpectation(self, count):
        outputString = 'The number of times the expected result (Quicksort time < Merge Sort time) fails to appear:', count
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
            
    def printMinimumPairedMergeSortTime(self, minimumPairedMergeSortTime):
        outputString = 'Minimum Merge Sort time with corresponding Quicksort time is (MS/QS format):', str(minimumPairedMergeSortTime)
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
        
    def printMinimumPairedQuicksortTime(self, minimumPairedQuicksortTime):
        outputString = 'Minimum Quicksort time with corresponding Merge Sort time is (MS/QS format):', str(minimumPairedQuicksortTime)
        with open(self.outFileName, 'a') as f:
            print(outputString, file=f)
        
class plotResults():
    def __init__(self):
        self.x = [10, 50, 100, 500, 1000, 5000, 10000]
        
    def plotAverageWallClockTime(self, allAverageMergeSortTimes, allAverageQuicksortTimes):
        y1 = allAverageMergeSortTimes
        y2 = allAverageQuicksortTimes
        plt.plot(self.x, y1, label='Merge Sort Times', marker='o')
        plt.plot(self.x, y2, label='Quicksort Times', marker='o')
        plt.xlabel("Array Size")
        plt.ylabel("Time (s)")
        plt.title("Average Wall Clock Time")
        plt.legend()
        plt.show()
    
    def plotMinimalWallClockTime(self, allMinimalMergeSortTimes, allMinimalQuicksortTimes):
        y1 = allMinimalMergeSortTimes
        y2 = allMinimalQuicksortTimes
        plt.plot(self.x, y1, label='Merge Sort Times', marker='o')
        plt.plot(self.x, y2, label='Quicksort Times', marker='o')
        plt.xlabel("Array Size")
        plt.ylabel("Time (s)")
        plt.title("Minimal Wall Clock Time")
        plt.legend()
        plt.show()
                
def gatherData(sequencialResultsFileName):
    instanceOfMergeSort = mergeSort()
    mergeSortTimes = instanceOfMergeSort.collectMergeSortTimes(sequencialResultsFileName)
    mergeSortTimesAverage = instanceOfMergeSort.findAverageMergeSortWallClockTime() 
    minimalMergeSortTime = instanceOfMergeSort.findMinimalMergeSortWallClockTime()
    
    instanceOfQuicksort = quicksort()
    quicksortTimes = instanceOfQuicksort.collectQuicksortTimes(sequencialResultsFileName)
    quicksortTimesAverage = instanceOfQuicksort.findAverageQuicksortWallClockTime() 
    minimalQuicksortTime = instanceOfQuicksort.findMinimalQuicksortWallClockTime() 
    
    instanceOfColumnStack = columnStack()
    stackOfTimes = instanceOfColumnStack.createStackOfSortTimes(mergeSortTimes, quicksortTimes)
    
    count = instanceOfColumnStack.findNumberOfResultsThatFailExpectation()
    
    minimumPairedMergeSortTime = instanceOfColumnStack.findMinimumTimeInPairsForMergeSort()
    minimumPairedQuicksortTime = instanceOfColumnStack.findMinimumTimeInPairsForQuicksort() 
    
    instanceOfPrintResults = printResults()
    instanceOfPrintResults.printHeader()
    
    instanceOfPrintResults.printAverageMergeSortWallClockTime(mergeSortTimesAverage)
    instanceOfPrintResults.printAverageQuicksortWllClockTime(quicksortTimesAverage)
    
    instanceOfPrintResults.printMinimalMergeSortWallClockTime(minimalMergeSortTime)
    instanceOfPrintResults.printMinimalQuickSortWallClockTime(minimalQuicksortTime)
    
    instanceOfPrintResults.printNumberOfResultsThatFailExpectation(count)
    
    instanceOfPrintResults.printMinimumPairedMergeSortTime(minimumPairedMergeSortTime)
    instanceOfPrintResults.printMinimumPairedQuicksortTime(minimumPairedQuicksortTime)

    outFileName = 'DivideAndConquerSortResults.txt'
    with open(outFileName, 'a') as f:
        print('', file=f)
        
for x in range(7):
    sequencialResultsFileName = 'DivideAndConquer_Results_' + str(x) + ".txt"        
    gatherData(sequencialResultsFileName)
instanceOfPlotResults = plotResults()
instanceOfPlotResults.plotAverageWallClockTime(allAverageMergeSortTimes, allAverageQuicksortTimes)
instanceOfPlotResults.plotMinimalWallClockTime(allMinimalMergeSortTimes, allMinimalQuicksortTimes)