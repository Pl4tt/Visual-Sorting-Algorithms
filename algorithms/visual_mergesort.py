from column import Column


def merge(arr, win, column_holder, low, middle, high):
    result = []
    l, m = low, middle

    while l < middle and m < high:
        if arr[l] < arr[m]:
            result.append(arr[l])
            l += 1
        else:
            result.append(arr[m])
            m += 1
    
    while l < middle:
        result.append(arr[l])
        l += 1
    
    while m < high:
        result.append(arr[m])
        m += 1
    
    for i in range(low, high):
        arr[i] = result[i-low]
        column_holder.update(win, i, Column(arr[i]/max(arr)))
        


def split(arr, win, column_holder, low, high):
    middle = (low+high) // 2

    if middle <= low:
        return
    
    split(arr, win, column_holder, middle, high)
    split(arr, win, column_holder, low, middle)
    merge(arr, win, column_holder, low, middle, high)

def merge_sort(arr, win, column_holder, low=0, high=None):
    if not high:
        high = len(arr)
    
    split(arr, win, column_holder, low, high)

    return arr

