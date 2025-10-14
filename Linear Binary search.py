def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def binary_search(arr, x):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == x:
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            h = m - 1
    return -1
arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to search: "))
lin = linear_search(arr, x)
arr.sort()
bin_ = binary_search(arr, x) 
print(f"Linear Search: {'Found at position ' + str(lin+1) if lin!=-1 else 'Not Found'}")
print(f"Binary Search: {'Found at position ' + str(bin_+1) if bin_!=-1 else 'Not Found'}")
