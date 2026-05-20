def find_peak_index(arr):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Пример 1

A1 = [1, 3, 8, 12, 4, 2]
p1 = find_peak_index(A1)
print(p1, A1[p1])

# Пример 2

A2 = [2, 4, 6, 8, 10, 15]
p2 = find_peak_index(A2)
print(p2, A2[p2])

# Пример 3

A3 = [20, 17, 13, 9, 5, 1]
p3 = find_peak_index(A3)
print(p3, A3[p3])