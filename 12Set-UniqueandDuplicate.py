def duplistore(lst):
    seen = set()
    duplicates = set()

    for number in lst:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


my = [1, 5, 6, 5, 1, 2, 3]

duplist = duplistore(my)

print(f"Original List: {my}")
print(f"Duplicate Elements: {duplist}")
