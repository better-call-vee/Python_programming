A = input("Enter elements for Set A (like, 1 2 3 4 5): ")
set_a = set(map(int, A.split()))

B = input("Enter elements for Set B (like, 4 5 6 7 8): ")
set_b = set(map(int, B.split()))

union_result = set_a | set_b
intersection_result = set_a & set_b
difference_result = set_a - set_b

print("\n--- Results ---")
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A | B):        {union_result}")
print(f"Intersection (A & B): {intersection_result}")
print(f"Difference (A - B):   {difference_result}")
print("-----tanvee-----")

