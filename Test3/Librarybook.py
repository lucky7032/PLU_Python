books = list(map(int, input("Enter Book IDs: ").split()))

search = int(input("Enter Book ID to search: "))

low = 0
high = len(books) - 1

while low <= high:
    mid = (low + high) // 2

    if books[mid] == search:
        print("Book Found at index:", mid)
        break
    elif search > books[mid]:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Book Not Found")