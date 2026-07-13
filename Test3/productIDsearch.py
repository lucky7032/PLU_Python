products = list(map(int, input("Enter product IDs: ").split()))

search = int(input("Enter product ID to search: "))

low = 0
high = len(products) - 1

while low <= high:
    mid = (low + high) // 2
    
    if products[mid] == search:
        print("Product found at index:", mid)
        break
    elif search > products[mid]:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Product Not Available")

    