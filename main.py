def isValidSubsequence(array, sequence):
    aPtr = 0
    sPtr = 0
    lenA = len(array)
    lenS = len(sequence)

    found = False

    while not found:
        while aPtr < lenA and array[aPtr] != sequence[sPtr]:
            aPtr += 1
    
        if not found and aPtr == lenA:
            return False
    
        if array[aPtr] == sequence[sPtr]:
            aPtr += 1
            sPtr += 1
            if sPtr == lenS:
                return True
    pass
