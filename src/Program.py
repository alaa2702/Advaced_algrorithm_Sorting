from MergeSort import merge_sort
from QuickSort import quick_sort


def process_list(option, lst):
    if option == '1':
        return lst
    elif option == '2':
        return list(reversed(lst))


def input_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please select from the given options.")


def get_list():
    mylist = []
    while True:
        try:
            n = int(input("Enter the number of elements "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(n):
        while True:
            try:
                element = int(input(f"Enter element {i + 1}: "))
                mylist.append(element)
                break
            except ValueError:
                print("Please enter a valid integer for the array element.")

    return mylist


def main():
    print("Welcome to the Sorting Algorithm Comparison Program!")

    list_choice = input_choice(
        "Choose the list type to be sorted:\n1. Sorted List\n2. Inversely Sorted List\nYour choice: ", ['1', '2'])
    sort_choice = input_choice(
        "Choose the sorting technique:\n1. Merge Sort\n2. Quick Sort\n3. All of them\nYour choice: ", ['1', '2', '3'])
    list_input = get_list()

    if sort_choice == '1':
        sorted_list, assignments_merge, comparisons_merge = merge_sort(list_input.copy())
        print("Merge Sort:")
        print("Sorted List:", process_list(list_choice, sorted_list))
        print("Assignments:", assignments_merge)
        print("Comparisons:", comparisons_merge)
    elif sort_choice == '2':
        sorted_list, assignments_quick, comparisons_quick, swap_quick = quick_sort(list_input.copy())
        print("Quick Sort:")
        print("Sorted List:", process_list(list_choice, sorted_list))
        print("Assignments:", assignments_quick)
        print("Comparisons:", comparisons_quick)
        print("Swaps", swap_quick)
    elif sort_choice == '3':
        sorted_list_merge, assignments_merge, comparisons_merge = merge_sort(list_input.copy())
        sorted_list_quick, assignments_quick, comparisons_quick, swap_quick = quick_sort(list_input.copy())

        print("Merge Sort:")
        print("Sorted List:", process_list(list_choice, sorted_list_merge))
        print("Assignments:", assignments_merge)
        print("Comparisons:", comparisons_merge)

        print("\nQuick Sort:")
        print("Sorted List:", process_list(list_choice, sorted_list_quick))
        print("Assignments:", assignments_quick)
        print("Comparisons:", comparisons_quick)
        print("Swaps", swap_quick)

        if comparisons_merge < comparisons_quick:
            print("\nMerge Sort performed fewer comparisons.")
        elif comparisons_merge > comparisons_quick:
            print("\nQuick Sort performed fewer comparisons.")
        else:
            print("\nBoth Merge Sort and Quick Sort performed the same number of comparisons.")

        if assignments_merge < assignments_quick:
            print("Merge Sort had fewer assignments.")
        elif assignments_merge > assignments_quick:
            print("Quick Sort had fewer assignments.")
        else:
            print("Both Merge Sort and Quick Sort had the same number of assignments.")


if __name__ == "__main__":
    main()
