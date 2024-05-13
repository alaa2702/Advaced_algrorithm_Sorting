def merge_sort(array):
    assignments = 0
    comparisons = 0
    if len(array) > 1:
        comparisons += 1
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]
        _, left_assignments, left_comparisons = merge_sort(left_array)
        _, right_assignments, right_comparisons = merge_sort(right_array)
        assignments += left_assignments + right_assignments
        comparisons += left_comparisons + right_comparisons
        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            comparisons += 1
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                assignments += 1

            else:
                array[k] = right_array[j]
                j += 1
                assignments += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
            assignments += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
            assignments += 1
    return array, assignments, comparisons
