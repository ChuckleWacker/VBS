# Function takes the index and doubles the value. If the index doesnt exist, then just returns the list.
def double_index(lst, index):
    if index < len(lst):
        lst[index] = lst[index] * 2
        return lst
    elif index >= len(lst):
        return lst
print(double_index([3, 8, -10, 12], 3))
print(double_index([3, 8, -10, 12], 4))


# Function removes the middle elements based on start / end arguments.
def remove_middle(lst, start, end):
    return lst[:start] + lst[end + 1:]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# Function calculates if an ITEM in the LIST shows up more than N times. Return True or False.
def more_than_n(lst, item, n):
    return lst.count(item) > n
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Function evaluates if item1 is >= item2, if so returns item1. Otherwise, returns item2.
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    return item2  # Returns item2 since item1 calculation didn't pass
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Function calculates whether the list is even or odd using a modulo, if even it calculates the middle two indexes,
# then figures pulls the value of that index, then adds the values of both indexes together and divides by 2. Else,
# if odd, we simply just needed to calculate the middle index and return it.
def middle_element(lst):
    if len(lst) % 2 == 0:  # Nothing left after dividing, assumes even number if true
        return (lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2
        # print(lst[int(len(lst) / 2) - 1])
        # print(lst[int(len(lst) / 2)])
        # print(lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)])
        # print((lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2)
    return lst[int(len(lst) / 2)]
print(middle_element([5, 2, -10, -4, 4, 5]))


# Function take the last two indexes in the list, adds them together, and appends it to the list. Repeat 3 times.
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst
print(append_sum([1, 1, 2]))


# Function compares length of list1 to list2, and returns largest list's last index.
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
      return lst1[-1]
    return lst2[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# Function combines list1 and list2 into new variable list3, sorts list3, then returns list3.
def combine_sort(lst1, lst2):
    lst3 = lst1 + lst2
    lst3.sort()
    return lst3
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# Function creates a "new_lst" that is based on a range using "i for i in range" between brackets along with length(lst)
# Then creates a "final_lst" that combines both lsts for later returning with.
def append_size(lst):
    new_lst = [i for i in range(1, (len(lst) + 1))]
    final_lst = lst + new_lst
    return final_lst
print(append_size([23, 42, 108]))


# Function immediately returns the new creation of an unnamed list, using "i for i in range" between brackets
def every_three_nums(start):
    return [i for i in range(start, 101, 3)]
print(every_three_nums(91))
