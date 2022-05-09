def quick_sort(array, start, end):
    if start < end:
        pi = partition(array, start, end)
        quick_sort(array, start, pi-1)
        quick_sort(array, pi+1, end)


def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[pivot_index], array[end] = array[end], array[pivot_index]

    return end

