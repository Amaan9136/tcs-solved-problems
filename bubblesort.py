# Bubble Sort Algorithm steps:

## 1. Start at the beginning of the list.
## 2. Compare each pair of adjacent elements.
## 3. If the first element is greater than the second, swap them.
## 4. Move to the next pair of elements and repeat.
## 5. Once you reach the end of the list, repeat the process, starting from the beginning again.
## 6. The largest unsorted element "bubbles" to the end of the list after each pass.
## 7. Repeat the process until no swaps are needed.

def bubble_sort_count(arr, ascending=True):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True
        if not swapped:
            break
    return swap_count

def min_swaps(arr):
    asc_swaps = bubble_sort_count(arr[:], ascending=True)  
    desc_swaps = bubble_sort_count(arr[:], ascending=False)  
    return min(asc_swaps, desc_swaps)

n = int(input())  
arr = list(map(int, input().split()))  

print(min_swaps(arr))
