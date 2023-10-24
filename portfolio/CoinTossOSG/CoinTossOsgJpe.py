import random

def coinToss():
    if (0.5 <= random.random()):
        return 1
    else :
        return 0
    
tossResult = coinToss()
print("Toss Result:", tossResult)

def testCoinFairness():
    #https://en.wikipedia.org/wiki/Checking_whether_a_coin_is_fair#:~:text=It%20is%20of%20course%20impossible,10%20heads%20in%2020%20flips.
    numberOfFlips = 27225
    numberOfHeads = 0
    acceptableErrorRate = 0.01
    acceptableOffset = numberOfFlips * acceptableErrorRate
    expectedNumberOfHeads = 0.5 * numberOfFlips 
    for i in range(numberOfFlips):
        numberOfHeads = numberOfHeads + coinToss()
        
    if ( 0 < ((expectedNumberOfHeads + acceptableOffset) - numberOfHeads) ):
        print("Fair Coin, Number of flips:", numberOfFlips, "Number of heads:", numberOfHeads, "acceptable offset:",acceptableOffset, "actual deviation", abs(expectedNumberOfHeads - numberOfHeads))
    else :
        print("Biased Coin, Number of flips:", numberOfFlips, "Number of heads:", numberOfHeads, "acceptable offset:",acceptableOffset, "actual deviation", abs(expectedNumberOfHeads - numberOfHeads))
        
testCoinFairness()

def setOfCoinsToss(numberOfCoins):
    numberOfHeads = 0
    for i in range(numberOfCoins):
        if(1 == coinToss()):
            numberOfHeads = numberOfHeads + 1
            #print("H",end='')
        #else:
            #print("T",end='')
    #print()
    return numberOfHeads

print(setOfCoinsToss(2))

import math
def countBalancedSets(numberOfCoinsInSet, numberOfRepeatsPerCoin):
    iterationCount  = numberOfCoinsInSet * numberOfRepeatsPerCoin
    numberOfHeadsForBalancedSet = numberOfCoinsInSet / 2
    numberOfBalancedSets = 0
    numberOfHeads = 0

    for i in range ( iterationCount ):
        numberOfHeads =  setOfCoinsToss(numberOfCoinsInSet)
        if( numberOfHeads == numberOfHeadsForBalancedSet):
            #print("Balanced set.")
            numberOfBalancedSets = numberOfBalancedSets + 1
        else:
            print("Not balanced set.")
        
    return numberOfBalancedSets

import time
numberOfCoinsInSet = 8
numberOfRepeatsPerCoin = 30000

for numberOfCoinsInSet in range(2, 12, 2):
    iterationCount  = numberOfCoinsInSet * numberOfRepeatsPerCoin
    startTime = time.time()
    numberOfBalancedSets = countBalancedSets(numberOfCoinsInSet, numberOfRepeatsPerCoin)
    stopTime = time.time()
    executionTime = stopTime - startTime
    print("if you have", numberOfCoinsInSet, "coins, and you flip them", iterationCount, "times, you get", numberOfBalancedSets,"balanced sets." )
    oddsOfBalancedSet = numberOfBalancedSets / iterationCount
    print("with",numberOfCoinsInSet,"coins, your odds of getting a balanced set are:", oddsOfBalancedSet)
    numberOfTimesNeededToGetABalancedSet = math.ceil(1.0/oddsOfBalancedSet)
    print("with",numberOfCoinsInSet,"coins, you would need to flip a full set", numberOfTimesNeededToGetABalancedSet, "times to find a balanced set." )
    print("this process took", executionTime)
