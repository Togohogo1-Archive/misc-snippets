items = []

while True:
    opt = int(input(
        "[1] Insert new item\n"
        "[2] Remove item\n"
        "[3] Print ranking\n"
        "[4] Print sorted\n"
    ))

    print(f"\n========= Total items: {len(items)} =========")

    if opt == 1:
        new_item = input("Name of the new item: ")

        left = 0
        right = len(items)

        if not items:
            items.append(new_item)
            continue

        while True:
            print(left, right, items)
            mid = (left + right) // 2
            yn = input(f"Is {new_item} better than {items[mid]}? [y/n]: ")

            # Search above it
            if yn.lower() == "y":
                left = mid + 1

                if left >= right:
                    items.insert(mid+1, new_item)
                    break

            # Search below it
            elif yn.lower() == "n":
                right = mid - 1
                print(left, right)
                if left >= right:
                    items.insert(mid, new_item)
                    break

    elif opt == 2:
        idx = int(input("Index to remove: "))
        print(f"Item removed: {items.pop(idx)}")

    elif opt == 3:
        for id, item in enumerate(items, start=1):
            print(f"{id}: {item}")

    elif opt == 4:
        for id, item in enumerate(sorted(items), start=1):
            print(f"{id}: {item}")

    print(f"========= Total items: {len(items)} =========\n")

'''
bug:
citrus, float, soda street, used to
'''
