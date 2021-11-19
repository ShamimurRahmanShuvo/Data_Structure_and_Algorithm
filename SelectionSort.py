def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        selection_sort(elements)
        print(f"sorted array: {elements}")