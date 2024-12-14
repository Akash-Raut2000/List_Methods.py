# Lists: Indexing, Slicing, and List Methods

# Sample list
sample_list = [10, 20, 30, 40, 50, 60]

# 1. Indexing
print("Original List:", sample_list)
print("First element:", sample_list[0])         # Accessing the first element
print("Last element:", sample_list[-1])        # Accessing the last element
print("3rd element:", sample_list[2])          # Accessing the 3rd element

# 2. Slicing
print("Slice (0-3):", sample_list[0:3])          # Slicing from index 0 to 2
print("Slice (3 to end):", sample_list[3:])     # From index 3 to the end
print("Slice (start to 3):", sample_list[:3])   # From start to index 2
print("Slice (step 2):", sample_list[::2])      # Every second element

# 3. List Methods
# a. Append (adds an element to the end of the list)
sample_list.append(70)
print("After append(70):", sample_list)

# b. Pop (removes and returns the last element or element at specified index)
popped_element = sample_list.pop()
print("After pop():", sample_list, "| Popped Element:", popped_element)

popped_at_index = sample_list.pop(2)
print("After pop(2):", sample_list, "| Popped Element at Index 2:", popped_at_index)

# c. Insert (inserts an element at a specific index)
sample_list.insert(2, 25)
print("After insert(2, 25):", sample_list)

# d. Remove (removes the first occurrence of a value)
sample_list.remove(25)
print("After remove(25):", sample_list)

# e. Extend (adds all elements of another list)
extra_list = [80, 90]
sample_list.extend(extra_list)
print("After extend([80, 90]):", sample_list)

# f. Reverse (reverses the order of elements)
sample_list.reverse()
print("After reverse():", sample_list)

# g. Sort (sorts the list in ascending order)
sample_list.sort()
print("After sort():", sample_list)

# h. Count (counts occurrences of a value)
count_20 = sample_list.count(20)
print("Count of 20:", count_20)

# i. Index (returns the index of the first occurrence of a value)
index_of_40 = sample_list.index(40)
print("Index of 40:", index_of_40)

# 4. Nested Lists and Membership
nested_list = [1, 2, [3, 4], 5]
print("Nested List:", nested_list)
print("Access nested element (3):", nested_list[2][0])
print("5 in nested_list:", 5 in nested_list)

# 5. List Comprehensions (bonus)
squared = [x**2 for x in sample_list]
print("List of squares:", squared)
