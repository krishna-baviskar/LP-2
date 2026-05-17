def selection_sort(arr):
    for i in range(len(arr)):
        # Greedily pick the minimum element from the unsorted part
        m_idx = arr.index(min(arr[i:]), i)
        arr[i], arr[m_idx] = arr[m_idx], arr[i]
    return arr

print("Sorted:", selection_sort([64, 25, 12, 22, 11]))
