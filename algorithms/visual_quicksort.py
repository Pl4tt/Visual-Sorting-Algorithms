def partition(arr, win, column_holder, low, high):
    pivot = arr[high]
    high_cache = high
    low_cache = low

    while low < high:
        while high >= low_cache and arr[high] >= pivot:
            high -= 1

        while low < high_cache and arr[low] < pivot:
            low += 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
            column_holder.swap(win, low, high)
            
    
    if arr[low] > pivot:
        arr[low], arr[high_cache] = arr[high_cache], arr[low]
        column_holder.swap(win, low, high_cache)

    return low

def quicksort(arr, win, column_holder, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = partition(arr, win, column_holder, low, high)
        quicksort(arr, win, column_holder, low, pivot-1)
        quicksort(arr, win, column_holder, pivot+1, high)
    
    return arr
