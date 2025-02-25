# Lists and Tuples in Python
# This script demonstrates various operations on lists and tuples, including counting, inserting, popping, slicing, sorting, and more.

# ------------------------------------------------------------------------------------
# Example List
# Lists are mutable and can store multiple items of different types.
# ------------------------------------------------------------------------------------

example_list = ["JD", "Cody", "Josh", "Your mom", "Your mom"]
print("Example List:", example_list)

# ------------------------------------------------------------------------------------
# Counting Occurrences in a List
# The `count()` method counts the number of occurrences of a specified item.
# ------------------------------------------------------------------------------------

# Count occurrences of "Your mom"
print("\nCounting Occurrences:")
print('Number of "Your mom" in example_list:', example_list.count("Your mom"))  # Output: 2

# ------------------------------------------------------------------------------------
# Example: Counting Votes
# A practical example of counting occurrences in a list of votes.
# ------------------------------------------------------------------------------------

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Count votes for each candidate
vote_count = [["Jake", votes.count("Jake")], 
              ["Laurie", votes.count("Laurie")], 
              ["Cassie", votes.count("Cassie")]]

print("\nVotes List:", votes)
print("Vote Count:", vote_count)

# ------------------------------------------------------------------------------------
# Inserting Items into a List
# The `insert()` method adds an item at a specified index.
# ------------------------------------------------------------------------------------

# Insert "Your Dad" at the second-to-last position
example_list.insert(-1, "Your Dad")
print("\nAfter Inserting 'Your Dad':", example_list)  # Output: ['JD', 'Cody', 'Josh', 'Your mom', 'Your Dad', 'Your mom']

# ------------------------------------------------------------------------------------
# Removing Items from a List
# The `pop()` method removes and returns the item at the specified index.
# If no index is provided, it removes the last item.
# ------------------------------------------------------------------------------------

# Remove the last item
print("\nPopped Item:", example_list.pop())  # Output: "Your mom"
print("List After Pop:", example_list)  # Output: ['JD', 'Cody', 'Josh', 'Your mom', 'Your Dad']

# ------------------------------------------------------------------------------------
# Creating Lists with `range()`
# The `range()` function generates a sequence of numbers, which can be converted to a list.
# ------------------------------------------------------------------------------------

# Range from 0 to 10 (not inclusive)
example_list_2 = range(10)
print("\nRange from 0 to 10:", list(example_list_2))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Range from 2 to 10 (not inclusive)
example_list_3 = range(2, 10)
print("Range from 2 to 10:", list(example_list_3))  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# Range from 2 to 10, incrementing by 2
example_list_4 = range(2, 10, 2)
print("Range from 2 to 10, incrementing by 2:", list(example_list_4))  # Output: [2, 4, 6, 8]

# ------------------------------------------------------------------------------------
# Finding the Length of a List
# The `len()` function returns the number of items in a list.
# ------------------------------------------------------------------------------------

# Length of example_list
print("\nLength of example_list:", len(example_list))  # Output: 5

# Length of example_list_2
print("Length of example_list_2:", len(example_list_2))  # Output: 10

# ------------------------------------------------------------------------------------
# Slicing Lists
# Slicing allows you to extract a portion of a list.
# ------------------------------------------------------------------------------------

example_list_5 = ["a", "b", "c", "d", "e", "f", "g"]

# Slice from index 0 to 5 (not inclusive)
example_list_5_sliced = example_list_5[0:5]
print("\nSliced List (0:5):", example_list_5_sliced)  # Output: ['a', 'b', 'c', 'd', 'e']

# First 5 elements
print("First 5 Elements:", example_list_5[:5])  # Output: ['a', 'b', 'c', 'd', 'e']

# First 3 elements
print("First 3 Elements:", example_list_5[:3])  # Output: ['a', 'b', 'c']

# Last 2 elements
print("Last 2 Elements:", example_list_5[-2:])  # Output: ['f', 'g']

# All elements except the last one
print("All Elements Except Last:", example_list_5[:-1])  # Output: ['a', 'b', 'c', 'd', 'e', 'f']

# ------------------------------------------------------------------------------------
# Sorting Lists
# The `sort()` method sorts the list in place, while `sorted()` returns a new sorted list.
# ------------------------------------------------------------------------------------

# Sort votes alphabetically
votes.sort()
print("\nSorted Votes:", votes)

# Sort votes in reverse order
votes.sort(reverse=True)
print("Reverse-Sorted Votes:", votes)

# Create a new sorted list
names_sorted = sorted(votes)
print("Names Sorted:", names_sorted)

# ------------------------------------------------------------------------------------
# Tuples in Python
# Tuples are similar to lists but are immutable (cannot be changed after creation).
# They are defined using parentheses `()`.
# ------------------------------------------------------------------------------------

# Example Tuple
example_tuple = ("JD", "Cody", "Josh", "Your mom")
print("\nExample Tuple:", example_tuple)

# Accessing Tuple Elements
print("First Element of Tuple:", example_tuple[0])  # Output: "JD"

# Counting Occurrences in a Tuple
print('Number of "Your mom" in example_tuple:', example_tuple.count("Your mom"))  # Output: 1

# Length of a Tuple
print("Length of example_tuple:", len(example_tuple))  # Output: 4

# Slicing Tuples
print("First 2 Elements of Tuple:", example_tuple[:2])  # Output: ("JD", "Cody")

# Immutable Nature of Tuples
# Uncommenting the following line will raise an error because tuples are immutable.
# example_tuple[0] = "New Name"  # TypeError: 'tuple' object does not support item assignment

# ------------------------------------------------------------------------------------
# Key Takeaways
# - Lists are mutable and versatile, allowing operations like insertion, deletion, and sorting.
# - Tuples are immutable and useful for storing fixed data.
# - Both lists and tuples support operations like slicing, counting, and finding length.
# ------------------------------------------------------------------------------------