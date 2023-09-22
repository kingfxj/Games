def main():
    numbers = [1,5,6,8,9,0,2,3]

    modifiedNumbers = changeNumArray(numbers)
    print(modifiedNumbers)

def addTwoNumbers(numOne, numTwo):
    return numOne + numTwo

def changeNumArray(numArray):
    modifiedNumbers = [0,0,0,0,0,0,0,0]
    for i in range(0, len(numArray)):
        modifiedNumbers[i] = numArray[i] + numArray[i+1] - 1
    return modifiedNumbers


main()