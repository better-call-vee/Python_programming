# === 1. Creating and Accessing Lists ===

# Creating a List
snacks = ["Chips", "Cake", "Soda", "Pizza"]
print("Initial list:", snacks)

# Accessing Items (Indexing starts at 0)
print("First snack (index 0):", snacks[0])
print("Last snack (negative index):", snacks[-1])

print("\n" + "=" * 20 + "\n")  # Separator for clarity

# === 2. Modifying a List ===

# Change an Item at a specific index
snacks[2] = "Juice"
print("After replacing 'Soda' with 'Juice':", snacks)

# Add an Item to the End (.append())
snacks.append("Cookies")
print("After appending 'Cookies':", snacks)

# Add an Item at a Specific Position (.insert())
# Let's insert "Tacos" at index 1
snacks.insert(1, "Tacos")
print("After inserting 'Tacos' at index 1:", snacks)

print("\n" + "=" * 20 + "\n")

# === 3. Removing Items from a List ===

# Remove a Specific Item by Value (.remove())
snacks.remove("Cake")
print("After removing 'Cake':", snacks)

# Remove an Item by Index (del)
# Let's remove the item at index 3 ('Pizza')
del snacks[3]
print("After deleting item at index 3:", snacks)

# Remove and Return the Last Item (.pop())
popped_snack = snacks.pop()
print("Popped snack:", popped_snack)
print("List after pop:", snacks)

# Empty the Entire List (.clear())
snacks.clear()
print("After clearing the list:", snacks)

print("\n" + "=" * 20 + "\n")

# === 4. Organizing and Combining Lists ===

# Sort a List (.sort())
full_table_unsorted = ["Chips", "Juice", "Cake", "Cookies"]
print("Unsorted table:", full_table_unsorted)
full_table_unsorted.sort()
print("Sorted table:", full_table_unsorted)

# Combine Two Lists (+)
table1 = ["Chips", "Juice"]
table2 = ["Cake", "Cookies"]
combined_table = table1 + table2
print("Combined table:", combined_table)

print("\n" + "=" * 20 + "\n")

# === 5. Nested Lists (A List of Lists) ===

# Each guest's bag of snacks
party_bags = [
    ["Chips", "Cookies"],  # Bag 0
    ["Cake", "Juice"],  # Bag 1
    ["Soda", "Pizza"],  # Bag 2
]
print("List of lists (party bags):", party_bags)

# Get the first bag (the entire list at index 0)
print("First bag:", party_bags[0])

# Get a specific item from a nested list: "Cake"
# It's in the second bag (index 1), and is the first item (index 0)
print("A specific item from a nested list:", party_bags[1][0])

# Looping through a nested list
print("--- Items in all bags ---")
for bag in party_bags:
    for item in bag:
        print(item)
