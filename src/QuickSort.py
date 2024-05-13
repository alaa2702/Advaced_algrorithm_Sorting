def quick_sort(array):
    assignments = 0
    comparisons = 0
    swap = 0

    def partition(arr, low, high):
        nonlocal assignments, comparisons, swap
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                assignments += 2
                swap += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swap += 1
        assignments += 2
        return i + 1

    def quick_sort_(arr, low, high):
        nonlocal assignments, comparisons, swap
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_(arr, low, pi - 1)
            quick_sort_(arr, pi + 1, high)

    quick_sort_(array, 0, len(array) - 1)
    return array, assignments, comparisons, swap
