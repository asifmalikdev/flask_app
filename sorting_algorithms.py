"""
Sorting Algorithms Implementation
==================================
This module contains implementations of various sorting algorithms in Python.
Each algorithm includes time complexity analysis and example usage.
"""


def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²) worst case, O(n) best case (if already sorted)
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list (in-place sorting, but returns for convenience)
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr


def selection_sort(arr):
    """
    Selection Sort Algorithm
    Time Complexity: O(n²) in all cases
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n²) worst case, O(n) best case
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr):
    """
    Merge Sort Algorithm
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr):
    """
    Quick Sort Algorithm
    Time Complexity: O(n log n) average case, O(n²) worst case
    Space Complexity: O(log n) average case
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    Quick Sort In-Place Algorithm
    Time Complexity: O(n log n) average case, O(n²) worst case
    Space Complexity: O(log n) average case
    
    Args:
        arr: List of comparable elements (modified in-place)
        low: Starting index
        high: Ending index
        
    Returns:
        None (sorts in-place)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    """Helper function for quick sort in-place"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr):
    """
    Heap Sort Algorithm
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """Helper function for heap sort"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr, max_val=None):
    """
    Counting Sort Algorithm
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k)
    
    Args:
        arr: List of non-negative integers
        max_val: Maximum value in array (if None, will be calculated)
        
    Returns:
        Sorted list
    """
    if not arr:
        return []
    
    if max_val is None:
        max_val = max(arr)
    
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result


def radix_sort(arr):
    """
    Radix Sort Algorithm
    Time Complexity: O(d * (n + k)) where d is number of digits
    Space Complexity: O(n + k)
    
    Args:
        arr: List of non-negative integers
        
    Returns:
        Sorted list
    """
    if not arr:
        return []
    
    arr = arr.copy()
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def counting_sort_by_digit(arr, exp):
    """Helper function for radix sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]


def bucket_sort(arr, num_buckets=None):
    """
    Bucket Sort Algorithm
    Time Complexity: O(n + k) average case, O(n²) worst case
    Space Complexity: O(n)
    
    Args:
        arr: List of floating point numbers between 0 and 1
        num_buckets: Number of buckets to use (default: len(arr))
        
    Returns:
        Sorted list
    """
    if not arr:
        return []
    
    if num_buckets is None:
        num_buckets = len(arr)
    
    buckets = [[] for _ in range(num_buckets)]
    
    for num in arr:
        bucket_idx = int(num * num_buckets)
        if bucket_idx == num_buckets:
            bucket_idx -= 1
        buckets[bucket_idx].append(num)
    
    for bucket in buckets:
        insertion_sort(bucket)
    
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result


def shell_sort(arr):
    """
    Shell Sort Algorithm
    Time Complexity: O(n²) worst case, O(n log n) best case
    Space Complexity: O(1)
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    arr = arr.copy()
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    return arr


def tim_sort(arr):
    """
    Tim Sort Algorithm (Python's built-in sort uses Tim Sort)
    Time Complexity: O(n log n) worst case, O(n) best case
    Space Complexity: O(n)
    
    This is a simplified version. Python's actual implementation is more complex.
    For production use, prefer Python's built-in sorted() function.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    # For simplicity, using merge sort as base
    # Real Tim Sort uses insertion sort for small arrays and merge sort for larger ones
    return merge_sort(arr)


# Example usage and testing
if __name__ == "__main__":
    # Test arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Shell Sort": shell_sort,
    }
    
    print("=" * 60)
    print("SORTING ALGORITHMS TEST")
    print("=" * 60)
    
    for test_arr in test_arrays:
        print(f"\nOriginal array: {test_arr}")
        print("-" * 60)
        
        for name, func in algorithms.items():
            try:
                sorted_arr = func(test_arr)
                print(f"{name:20s}: {sorted_arr}")
            except Exception as e:
                print(f"{name:20s}: Error - {e}")
    
    # Test counting sort with integers
    print("\n" + "=" * 60)
    print("COUNTING SORT TEST (for integers)")
    print("=" * 60)
    int_array = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original: {int_array}")
    print(f"Sorted:   {counting_sort(int_array)}")
    
    # Test radix sort
    print("\n" + "=" * 60)
    print("RADIX SORT TEST")
    print("=" * 60)
    radix_array = [170, 45, 75, 90, 2, 802, 24, 66]
    print(f"Original: {radix_array}")
    print(f"Sorted:   {radix_sort(radix_array)}")
    
    # Test bucket sort
    print("\n" + "=" * 60)
    print("BUCKET SORT TEST (for floats 0-1)")
    print("=" * 60)
    bucket_array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"Original: {bucket_array}")
    print(f"Sorted:   {bucket_sort(bucket_array)}")

