def insertion_sort(arr):
    """
    Perform insertion sort on the given array.
    
    Input:
    - arr: A list of comparable elements
    
    Output:
    - The same list, sorted in ascending order
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    for j in range(1, len(arr)):
        # Key element to be inserted
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


def main():
    # Example usage
    test_array = [5, 2, 4, 6, 1, 3]
    print("Original array:", test_array)
    
    sorted_array = insertion_sort(test_array)
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    main()
