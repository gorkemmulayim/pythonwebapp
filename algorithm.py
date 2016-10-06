def isDistinct(array: list, startIndex: int, endIndex: int) -> bool:
    """ 
        This method searches the given array from startIndex to endIndex
        for same elements. If all the elements are distinct in the given range,
        returns True, else returns False.

    Args:
        array (list): Array to be iterater.
        startIndex (int): Start index, can be negative for backwards search.
        endIndex (int): End index, can be negative for backwards search.

    Returns:
        bool: The return value. True if all the elements are distinct, False otherwise.

    Raises:
        IndexError: If startIndex and endIndex are out of range. Method will return
            successfully if finds an answer before access the array with wrong index.

    """
    if len(array) == 0:
        return False
    if len(array) == 1:
        return True
    if abs(startIndex) > len(array) or abs(endIndex) > len(array):
        raise IndexError
    else:
        if startIndex < 0:
            startIndex += len(array)
        if endIndex < 0:
            endIndex += len(array)
    if startIndex == endIndex:
        return True
    elif startIndex < endIndex:
        step = 1;
    else:
        step = -1;
    for i in range(startIndex, endIndex, step):
        for j in range(startIndex, endIndex, step):
            if array[i] == array[j] and i != j:
                return False
    return True
