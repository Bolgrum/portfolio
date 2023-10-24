import random
from warnings import filterwarnings
filterwarnings("ignore", category=DeprecationWarning)
def coinToss():
    if (0.5 <= random.random()):
        return 1
    else :
        return 0

def testCoinFairness():
    #https://en.wikipedia.org/wiki/Checking_whether_a_coin_is_fair#:~:text=It%20is%20of%20course%20impossible,10%20heads%20in%2020%20flips.
    numberOfFlips = 30000
    numberOfHeads = 0
    acceptableErrorRate = 0.01
    acceptableOffset = numberOfFlips * acceptableErrorRate
    expectedNumberOfHeads = 0.5 * numberOfFlips 
    for i in range(numberOfFlips):
        numberOfHeads = numberOfHeads + coinToss()
        
    if (0 < ((expectedNumberOfHeads + acceptableOffset) - numberOfHeads)):
        temp = 0
    else :
        outFileName = "results" + str(i) + ".txt"
        outputString = "Biased Coin, Number of flips:", str(numberOfFlips), "Number of heads:", str(numberOfHeads), "acceptable offset:", str(acceptableOffset), "actual deviation", str(abs(expectedNumberOfHeads - numberOfHeads))
        with open(outFileName, 'w') as f:
            print(outputString, file=f)
        
testCoinFairness()

def setOfCoinsToss(numberOfCoins):
    numberOfHeads = 0
    for i in range(numberOfCoins):
        if(1 == coinToss()):
            numberOfHeads = numberOfHeads + 1
    return numberOfHeads

print("")

import math
def countBalancedSets(numberOfCoinsInSet, numberOfRepeatsPerCoin):
    iterationCount  = numberOfCoinsInSet * numberOfRepeatsPerCoin
    numberOfHeadsForBalancedSet = numberOfCoinsInSet / 2
    numberOfBalancedSets = 0
    numberOfHeads = 0

    for i in range (iterationCount):
        numberOfHeads =  setOfCoinsToss(numberOfCoinsInSet)
        if( numberOfHeads == numberOfHeadsForBalancedS4et):
            numberOfBalancedSets = numberOfBalancedSets + 1
        
    return numberOfBalancedSets

def scaleIncrement(num, scale = 10):
    return(num * scale + 1)

numberOfRepeatsPerCoin = 10000

import sys
i = sys.argv[1]
numberOfCoinsInSet = int(sys.argv[2])

fullChance = (math.factorial(numberOfCoinsInSet)) / ((math.factorial(numberOfCoinsInSet / 2)) * (math.factorial(numberOfCoinsInSet / 2)) * (2 ** numberOfCoinsInSet))
chance = round(fullChance, 5)
iterationCount  = numberOfCoinsInSet * numberOfRepeatsPerCoin
numberOfBalancedSets = countBalancedSets(numberOfCoinsInSet, numberOfRepeatsPerCoin)
results = (scaleIncrement(numberOfCoinsInSet))
outFileName = "CoinFlipResults" + str(i) + ".txt"

# Results file should read, in order:
# 1. Mathematical probability of getting x number of heads
# 2. Number of coins per set
# 3. Number of balanced sets / iterations made 
outputString = str(chance) + ", " + str(numberOfCoinsInSet) + ", " + str(numberOfBalancedSets / iterationCount) + "\n"
with open(outFileName, 'w') as f:
    print(outputString, file=f)
