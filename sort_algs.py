def selection_sort(array: list[int]) -> None:
    n = len(array)
    i = 0
    while i < n - 1:
        min_index = i
        min_value = array[i]
        j = i + 1
        while j < n:
            if array[j] < min_value:
                min_value = array[j]
                min_index = j
            j += 1
        array[min_index] = array[i]
        array[i] = min_value
        i += 1

def bubble_sort(array: list[int]) -> None:
    # TODO: add early exit
    n = len(array)
    i = n - 1
    while i > 0:
        j = 0
        while j < i:
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            j += 1
        i -= 1

def insertion_sort(array: list[int]) -> None:
    n = len(array)
    i = 1
    while i < n:
        curr_value = array[i]
        j = i - 1
        while j >= 0 and curr_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = curr_value
        i += 1

if __name__ == "__main__":
    nums = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    nums2 = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    nums3 = [7, 4, 6, 9, 10, 2, 5, 3, 8]

    print(nums)
    print("Selection Sort")
    selection_sort(nums)
    print(nums)

    print("Bubble Sort")
    bubble_sort(nums2)
    print(nums2)

    print("Insertion Sort")
    insertion_sort(nums3)
    print(nums3)
