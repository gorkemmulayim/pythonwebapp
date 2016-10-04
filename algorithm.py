def containsSameElement(array, startIndex, endIndex):
    if len(array) == 0:
        return False;
    for i in range(startIndex, endIndex):
        for j in range(startIndex, endIndex):
            if array[i] == array[j]:
                return True;
    return False;
