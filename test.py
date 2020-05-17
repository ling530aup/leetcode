# Binary search

def bi_search(arr, key):
    left, right = 0, len(arr)
    while left < right:
        mid = int((left + right) / 2)
        if key > arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid
        else:
            return mid
    print("Not found")
    return mid

if __name__ == '__main__':
    ls = [1, 2, 4, 6, 7, 9]
    key = 3
    index = bi_search(ls, key)
    print("index = ", index)
