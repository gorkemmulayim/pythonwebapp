def isDistinct(array, index1, index2):
    """ 
        This method searches the given array from index1 to index2
        for same elements. If all the elements are distinct in the given range,
        returns True, else returns False.

    Args:
        array (list): Array to be iterated.
        index1 (int): Start index, can be negative for backwards search.
        index2 (int): End index, can be negative for backwards search.

    Returns:
        bool: The return value. True if all the elements are distinct, False otherwise.
            Returns False if array contains no element.

    Raises:
        IndexError: If index1 and index2 are out of range. Method will return
            False if it encounters same elements before accessing the array
            with wrong index. Else raises IndexError.

    """
    startIndex = int(index1)
    endIndex = int(index2)
    if not isinstance(array, list):
        return False
    if len(array) == 0:
        return False
    if abs(startIndex) > len(array) or abs(endIndex) > len(array):
        raise IndexError
    if startIndex < 0:
        startIndex += len(array)
    if endIndex < 0:
        endIndex += len(array)
    if startIndex == endIndex:
        return True
    if startIndex < endIndex:
        step = 1;
    else:
        step = -1;
    for i in range(startIndex, endIndex + 1, step):
        for j in range(startIndex, endIndex + 1, step):
            if array[i] == array[j] and i != j:
                return False
    return True
