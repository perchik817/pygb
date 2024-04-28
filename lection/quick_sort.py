def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivor = arr[0]
    less = [i for i in arr[1:] if i <= pivor]
    greater = [i for i in arr[1:] if i > pivor]

    return quick_sort(less) + [pivor] + quick_sort(greater)
