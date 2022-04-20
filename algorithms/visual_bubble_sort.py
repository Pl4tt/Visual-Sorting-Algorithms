def bubble_sort(arr, win, column_holder):
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                column_holder.swap(win, i, i+1)
            
    return arr