# ---------------------------------------------------
# GitHub Username : KatrinaGW
#
# Exercise 2: Unfair Dice
# ---------------------------------------------------

import random

def createRunningSum(values):
    """
    Create a list containing the running sum of a list a float numbers
    Arguments :
        values (float list): A list of decimal float numbers
    Returns:
        newList (float list): The running sum of the given float list
    """

    #Create an empty new list and initialize the running sum to 0
    newList = []
    runningSum = 0

    #Add each value in the float list to the sum of the previous values,
    #then append the new sum to the running sum list
    for value in values:
        runningSum+=value
        newList.append(runningSum)

    return newList

def getDiceSide(decimal, runningSum):
    """ Map a given decimal number between 0 and 1 to a side of a dice.
    Arguments :
        decimal (float): A decimal number that will always be inclusively between 0 and 1
        runningSum (float list): A running sum list of floats that always go from 0 to 1. The
                                    difference between two elements is the probability of the
                                    higher one being rolled.

    Returns:
        index (int): The side of the dice which the decimal value was mapped to
    """

    #Set the bigger number, and the list index, to be 0
    biggerNumber = 0
    index = 0

    #Find index of the first value in the running sum which is higher than 
    #the given decimal number
    while(decimal>=biggerNumber and index<len(runningSum)):
        biggerNumber = runningSum[index]
        #Add 1 to the index because the element at the (n-1) index stores the
        #roll probability for the nth dice side
        index+=1

    return index


def biased_rolls(probabilities, randomSeed, rollNumber):
    """ Simulate rollNumber rolls of a biased m-sided die and return
    a list containing the results. 

    Arguments:
        probabilities: a list of the probabilities of rolling the 
                   number on each side of the m-sided die. The list  
                   will always have the length m (m >= 2), where m is 
                   the number of sides numbered 1 to m. Therefore,  
                   for example, the probability stored at index 0 in 
                   the list is the probability of rolling a 1 on
                   the m-sided die.
        randomSeed: the seed to use when initializing the PRNG
        rollNumber: the number of rolls to return

    Return:
        rolls: a list (of length rollNumber) containing each of the rollNumber rolls of the 
               biased die, in the order they were generated.
    """

    #Set the seed for the pseudo random module
    random.seed(randomSeed)

    #Get the running sum of the probabilities list
    runningSum = createRunningSum(probabilities)

    rolls=[]

    #For the given number of rolls, generate a pseudo-random fraction and map it to 
    #a side of the dice based on the given dice side probabilities
    for index in range(rollNumber):
        #Get a pseudo-random decimal value inclusively between 0 and 1
        rollValue = random.random()
        #Get the dice side which the rolled value represents and append it to the list of rolls
        rolls.append(getDiceSide(rollValue, runningSum))

    return rolls

def draw_histogram(sides, rolls, width):
    """
    Create a horiztonal histogram representing the frequency of the dice sides being rolled, mapped 
    to a fixed width

    Arguments :
        sides(int): The number of sides of the dice
        rolls(int list): A list containing the dice sides which were rolled
        width(int): The fixed width of the histogram in String characters. (The largest
        bar will be this width and all the other bars will be scaled accordingly)

    Returns:
        None (but prints the histogram to standard output)
    """

    #Initialize an empty list where the element stored at the (n-1) index is the
    #number of rolls for the nth dice side
    rollCounts = []

    #Find the number of times each side was rolled
    for side in range(1, sides+1):
        rollCount = rolls.count(side)
        rollCounts.append(rollCount)

    #Find which side was rolled the most
    biggestRolls = max(rollCounts)

    #Create a header for the histogram
    histogram = "Frequency Histogram: {}-sided Die\n".format(sides)

    #Print a frequency bar for each side's number of rolls
    for index in range(0, sides):
        #The side with the largest number of rolls has the maximum width,
        #find the scaled width of each side's bar by multiplying its roll count 
        #by the maximum width and dividing it by the largest roll count
        scaledWidth = rollCounts[index]/biggestRolls * width

        #Use '#' symbols to represent the dice side's bar's scaled width
        scaledWidth=int(round(scaledWidth, 0))
        widthSymbols = scaledWidth*"#"
        #Add '-' symbols to represent the empty space between the specific width and the largest width
        emptySpace = int(width - scaledWidth)
        emptySymbols = emptySpace*"-"
        #Add the newline character to the end of the bar only if the bar is not the last one to be created
        if(index == sides - 1):
            histogram = "{}{}.{}{}".format(histogram, index+1, widthSymbols, emptySymbols)
        else:
            histogram = "{}{}.{}{}\n".format(histogram, index+1, widthSymbols, emptySymbols)

    print(histogram)


def main():
    #Test inputs to run
    rolls = biased_rolls([1/12, 1/4, 1/3, 1/12, 1/12, 1/6], 2**32-1, 20)
    print(draw_histogram(6, rolls, 50))
    rolls = biased_rolls([1/4, 1/6, 1/12, 1/12, 1/4, 1/6], 42, 200)
    print(draw_histogram(6, rolls, 10)) 
    rolls = biased_rolls([1/3, 1/3, 1/3], (2**32)-1, 1000)
    print(draw_histogram(3, rolls, 10))
    rolls = [3, 2, 3, 2, 3, 3, 4, 6, 2, 6, 3, 2, 6, 2, 5, 5, 3, 4, 4, 2]
    print(draw_histogram(6, rolls, 50))

if __name__ == '__main__':
    main()
