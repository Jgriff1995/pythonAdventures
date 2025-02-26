# Coding Challenge 2: Append sum of elements of list 3 times
# takes in a list, of n length, and adds the 2nd to last and last element together 3 times 
# adds sums to end of list, and returns modified list
def append_sum(my_list):
    [my_list.append(my_list[-2] + my_list[-1]) for i in range(3)]
    return my_list

print(append_sum([1,1,2]))
print(append_sum([2,5]))

# Coding Challenge 3: Conveyr Belts
# check if the length of items on conv1 is greater than or equal to conv2
# if it is true, return the last element of first list
# if not, return last element of second list
def larger_list(my_list1, my_list2):
    if len(my_list1) >= len(my_list2):
        return my_list1[-1]
    else:
        return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Coding Challenge 4: More Than N
# takes in a list, an item to look for, and a number n that is the minimum req
def more_than_n(my_list,item,n):
    if my_list.count(item) > n:
        return True
    else:
        return False
    
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Coding Challenge 5: Combine Sort
# takes in two lists, concatonates them, and sorts them
def combine_sort(my_list1, my_list2):
    return sorted(my_list1 + my_list2)


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Coding Challenge 6: Divisible by 10
# Takes in a list of numbers, initializes a counter
# For every number divis by 10 in the list, add 1 to counter
def divisible_by_ten(nums):
    counter =0
    for i in nums:
        if i % 10 == 0:
            counter+=1
    return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Coding Challenge 7: Greetings
# Takes in a list of names, and returns a new list that contiains
# "Hello, <insert_name>" gathered from the input of names

# Regular way
def add_greetings(names):
    new_greetings = []
    for name in names:
        new_greetings.append(f"Hello, {name}")
    return new_greetings

# Condensed "elegant" one line loop way
def add_greetings2(names):
    new_greetings = [f"Hello, {name}" for name in names]
    return new_greetings

print(add_greetings(["Owen", "Max", "Sophie"]))
print(add_greetings2(["JD", "Cody", "Pinky"]))


# Coding Challenge 8: Delete starting Even Numbers
# two implementations, using for ( less-elegant) and while (more elegant) loops

# for loop implementation 
def delete_starting_evens(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            return my_list[i:]
    return []

# while Loop implementation   
def delete_starting_evens2(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]
        pass
    return my_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

print(delete_starting_evens2([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens2([4, 8, 10]))

# Coding CHallenge 9: Odd Indices
# Takes in a list of numbers, iterates over them, skipping even indices
# returns the numbers located at the odd indices as a new list 

# My approach
def odd_indices(my_list):
    new_list = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]
    return new_list

# 2nd approach using parts of solution given after exercise
# biggest change here is the range, starting at 1 and incrementing by 2 until
# len of my_list ensures that only odd indices are chosen, vs checking each one
# to see if the index is odd or even
def odd_indices2(my_list):
    new_list = [my_list[i] for i in range(1,len(my_list),2)]
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))
print(odd_indices2([4, 3, 7, 10, 11, -2]))

# Coding Challenge 10: Exponents
# given two inputs, bases and powers, calculate all the base's powers depending on how
# many are in each. i.e. bases: [2,3,4] are our base values, and we want to raise
# each base to given powers, powers: [1,2,3], add them to a list and return it
# should return 2^1, 2^2, 2^3, 3^1, 3^2.. etc.

# My first approach (long, correct, non optimized)
def exponents(bases,powers):
    answers = []
    for base in bases:
        for power in powers:
            answers.append(base ** power)
    return answers

print(exponents([2, 3, 4], [1, 2, 3]))

# Second Approach after researching nested one line for loops
# was able to condense this down to a single line of logic (excluding return)

def exponents2(bases,powers):
    answers = [base ** power for base in bases for power in powers]
    # <new_list> = [<operation> for <element> in <first_list> for <element> in <second_list>]
    return answers

print(exponents2([2, 3, 4], [1, 2, 3]))

# Coding Challenge 11: Larger Sum
# take in two lists, find the sums of each list individually
# compare them, if list1 > or equal to list2 sum, return LIST1 (not the sum)
# else, check the max of the 2, if it's list1, return list1, else return list2
def larger_sum(lst1,lst2):
    sum = 0
    sum2 = 0
    for i in lst1:
        sum += i
    for i in lst2:
        sum2 += i
    if sum >= sum2:
        return lst1
    
    if max(sum,sum2) == sum:
        return lst1
    else:
        return lst2
        
print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2nd Approach (Not ALL my own work, part LLM)
def larger_sum2(list1,list2):
    return list1 if sum(list1) >= sum(list2) else list2

# Notes - did not know about the sum function it adds all the elements
# in a given list, if i had known this, the solution would've been much clearer
# although to be fair, i don't believe we've covered sums in the course yet

print(larger_sum2([1, 9, 5], [2, 3, 7]))