# Function "Divisible by 10"
# Create a function that takes a list as a parameter. Return the amount of numbers in that list that are divisible by 10
def divisible_by_ten(nums):
    lst = [nums[i] for i in range(0, len(nums)) if nums[i] % 10 == 0]
    return len(lst)
print(divisible_by_ten([20, 25, 30, 35, 40]))

# Function "Greetings"
# Create a function that takes a list of strings as a parameter,  adds the string "Hello, " in front of each name, and
# returns as a new list containing the greetings.
def add_greetings(names):
    lst = ["Hello, " + name for name in names]
    return lst
print(add_greetings(["Owen", "Max", "Sophie"]))


# Function "Delete Lists Starting Even Numbers"
def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:  # While length of list is greater than 0 and list's first value is even
        lst = lst[1:]  # Incrementally slice the list, as list now slices the first index value
    return lst  # Return the list from the point of where you are currently at
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# Function "Odd Numbers" to create a new list comprised of only odd numbers from the original list
def odd_indices(lst):
    new_lst = [i for i in lst if i % 2 != 0 or i < 0]
    return new_lst
print(odd_indices([4, 3, 7, 10, 11, -2]))


# Function "Odd Indices" to create a new list comprised of only odd indices from the original list
def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst
print(odd_indices([4, 3, 7, 10, 11, -2]))


# Function "Exponents" that calculates exponents between two lists
def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst
print(exponents([2, 3, 4], [1, 2, 3]))


# Function "Largest List Sum" calculates what list has the larger sum
def larger_sum(lst1, lst2):
    sum_lst1 = 0; sum_lst2 = 0
    for i in lst1:
        sum_lst1 += i
    for i in lst2:
        sum_lst2 += i
    if sum_lst2 > sum_lst1:
        return lst2
    else:
        return lst1
print(larger_sum([1, 9, 5], [2, 3, 7]))


# Function "Over 9000" adds each item in the list, checking if it has exceeded the 9000, if not it continue to add.
def over_nine_thousand(lst):
    sum = 0
    for i in lst:
        sum += i
        if sum > 9000:
            break
    return sum
print(over_nine_thousand([8000, 900, 120, 5000]))


# Function "Max Number" checks through a list and outputs the highest number found.
def max_num(nums):
    temp = nums[0]
    for i in nums:
        if i > temp:
            temp = i
    return temp
print(max_num([50, -10, 0, 75, 20]))


# Function "Same Numbers" compares two lists and if the same index numbers match, it returns that index in a new list.
def same_values(lst1, lst2):
    new_lst = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append(index)
    return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# Function takes two lists of the same size, and returns true if list1 is the same as list2 backwards/reversed.
# Example would be List1 = [1,2,3] and List2 = [3,2,1] is the same as list1 but backwards/reversed.
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True
print(reversed_list([1, 2, 3], [3, 2, 1]))  # Returns True
print(reversed_list([1, 5, 3], [3, 2, 1]))  # Returns False
