# Types of List Usage

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

age = []  # Creates an empty list called "age"

age.append(42)  # Adds the number 42 to empty list called "age"

all_ages = age + [32, 41, 29]  # Adding a series of integers to a list called "all_ages"

name_and_age = zip(first_names, all_ages)  # Combining to different lists with the zip function

ids = range(0, 4)  # Creating a list using a range, so the list will populated with 0, 1, 2, 3
print(ids)

friends = ["Dan"]
friends = friends + ["Cheyne"] # Adding Cheyne to friends list
print(friends)

# This example shows that you can easily select the last item in a list by just using [-1], even if you dont know how..
# many items the list contains.
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element, element5)

# This example shows how we can call up specific parts of the list, called Slicing.
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:4]
middle = suitcase[2:4]
print(beginning)  # Will print "shirt shirt pants pants"
print(middle)  # Will print "pants pants"

# Additional ways to splice using an assumed range from start or from end
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
print(start)
end = suitcase[-2:]
print(end)

# This example shows how to count how many times something is in a list
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count("Jake")
print(jake_votes)   # Prints 9 as the number of times Jake was found in list "votes"
laurie_votes = votes.count("Laurie")
print(laurie_votes)  # Prints 6 as the number of times Laurie was found in list "votes"
cassie_votes = votes.count("Cassie")
print(cassie_votes)  # Prints 5 as the number of times Cassie was found in list "votes"


# This example shows how to sort a list
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace']
addresses.sort()
print(addresses)
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
sorted_cities = cities.sort()
print(sorted_cities)  # This will print None because you cannot assign a variable to a sorting of a list
print(cities)

# This example shows how to sort a list if you want to create a new variable with the sorting (as attempted above in
# lines 59 and 60
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

# This example shows an assortment of list manipulation occurring.
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)  # Create a new variable to track how many items are in "inventory"
first = inventory[0]  # Creates a new variable to save the first item in "inventory"
last = inventory[-1]  # Creates a new variable to save the last item in "inventory"
inventory_2_6 = inventory[2:6]  # Creates a new variable to save indexed items 2 through 5 from "inventory"
first_3 = inventory[:3]  # Creates a new variable to save the first three items from "inventory"
twin_beds = inventory.count("twin bed")  # Creates a new variable to store how many twin beds there are
inventory.sort()  # Sorts inventory list

# This function checks the length of the list and sees if the index falls within the defined range, if so
# then updates the indexed value on the list to be * 2, then return list. Otherwise, if the index falls outside the
# range of the length of the list then just return the current list.
def double_index(lst, index):
    if len(lst) > index:
        lst[index] = lst[index] * 2
        return lst
    elif len(lst) <= index:
        return lst
print(double_index([3, 8, -10, 12], 0))  # Index 0 returns as 6
print(double_index([3, 8, -10, 12], 1))  # Index 1 returns as 16
print(double_index([3, 8, -10, 12], 2))  # Index 2 returns as -20
print(double_index([3, 8, -10, 12], 3))  # Index 3 returns as 24
print(double_index([3, 8, -10, 12], 4))  # Index 4 falls outside the index range, so returns [3, 8, -10, 12]



