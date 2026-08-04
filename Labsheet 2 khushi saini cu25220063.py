# Linear Search Implementation using python

arr = [10, 20, 30, 40, 50]
key = int(input("Enter the number to search: "))
found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
    

# Binary Search Implementation using python


arr = [10, 20, 30, 40, 50, 60, 70]
key = int(input("Enter the number to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index:", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")