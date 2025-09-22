attendance = [18, 20, 19, 15, 21]

# Check attendance each day
for x in attendance:
    if x >= 20:
        print("Full Attendance")
    else:
        print("Not Full")

# Count days with full attendance
def fullClassCount(attendance):
    a = 0
    for y in attendance:
        if y >= 20:
            a += 1
    return a

print("Full Day Count:", fullClassCount(attendance))

# Total attendance
def totalattendance(attendance):
    total = 0
    for z in attendance:
        total += z
    return total

print("Total Attendance for all 5 days:", totalattendance(attendance))

# Grocery list operations
groceryList = ["milk", "bread", "egg"]

def add_item(item):
    groceryList.append(item)
    return groceryList

print("Added List:", add_item("Mango"))

def remove_last_item():
    if groceryList:  
        groceryList.pop()
    return groceryList

print("Remove Last Item:", remove_last_item())

# Lambda for display
display_item = lambda item: print(f"Item: {item}")
for x in groceryList:
    display_item(x)

# Recursive character count
def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("Recursive: Total no of characters in all items:", count_characters(groceryList))
