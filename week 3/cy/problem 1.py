
# Input: Initial shopping list
# Input: Initial shopping list
shopping_list = input().split()

# Input: Item to remove
item_to_remove = input()

# Input: New items to add
new_items = input().split()

# Print the initial shopping list
print("List1:", [int(x) if x.isdigit() else x for x in shopping_list])

# Try to remove the item
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print("List after removal:", [int(x) if x.isdigit() else x for x in shopping_list])
else:
    print("Element not found in the list")

# Add new items
shopping_list.extend(new_items)

# Final list output
print("Final list:", [int(x) if x.isdigit() else x for x in shopping_list])
