def solution(array):
    if not array:
        raise Exception
    
    if array[0] < array[-1]:
        raise Exception
    
    index1, index2 = 0, len(array) - 1
    mid = index1
    
    while array[index1] > array[index2]:
        
        mid = int((index1 + index2) / 2)
        
        if index2 - index1 == 1:
            mid = index2
            break
        
        if array[mid] > array[index1] and array[mid] > array[index2]:
            index1 = mid
        
        if array[mid] < array[index1] and array[mid] < array[index2]:
            index2 = mid
    
    return array[mid]


array = [4, 5, 6, 7, 8, 9, 10, 11, 2, 3]

print(solution(array))
