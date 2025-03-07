def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[-1]
    left, right = [],[]
    for elem in arr[:-1]:
        if elem<=pivot:
            left.append(elem)
        else:
            right.append(elem)
    return quick_sort(left)+[pivot]+quick_sort(right)