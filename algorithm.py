def containsSameElement(array, startIndex, endIndex):
    if len(array) == 0 or len(array) == 1:
        return False
    if abs(startIndex) > len(array) or abs(endIndex) > len(array):
        raise IndexError
    else:
        if startIndex < 0:
            startIndex += len(array)
        if endIndex < 0:
            endIndex += len(array)
    if startIndex == endIndex:
        return False
    elif startIndex < endIndex:
        step = 1;
    else:
        step = -1;
    for i in range(startIndex, endIndex, step):
        for j in range(startIndex, endIndex, step):
            if array[i] == array[j] and i != j:
                return True
    return False
