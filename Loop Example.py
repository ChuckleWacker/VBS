# Uses each element in a list, also known as iterating.
#for < temporary variable > in < list variable >:
#    < action >


#Example of a "for <variable> in <list>:
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
# Variation of ways to essentially create a temp variable to iterate through the defined list.
for i in board_games:
    print(i)
for game in board_games:
    print(game)
for whatever in board_games:
    print(whatever)
# Variation of ways to essentially create a temp variable to iterate through the defined list.
for i in sport_games:
    print(i)
for game in sport_games:
    print(game)
for whatever in sport_games:
    print(whatever)


# Example of "for <temp variable> in range(5), take the sum and add 1 each time you iterate through the range.
# We iterate 5 times total.
sum = 0
for i in range(5):
    sum += 1
    print(sum)


# Example of "for <temp variable> in range(10), take the awesome variable and add 1 each time you iterate through range.
# We iterate 10 times total.
awesomeness = 0
for i in range(10):
    awesomeness += 1
    print("Mat has been awesome {} number of times".format(awesomeness))


# Example of taking a dog breed list, and iterating through it to print each dog.
dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)


# Example of looping through each item in list A, then adding each item to list B.
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for students in students_period_A:
    students_period_B.append(students)
    print(students)
print(students_period_B)


# Example of going through a list of dogs and when you find the one you want, you stop iterating using "break"
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'
for dogs in dog_breeds_available_for_adoption:
    print(dogs)
    if dogs == dog_breed_I_want:
        print("They have the dog I want!")
        break


# Example goes through "ages" list and if people/iteration are less than 21 it uses continue to skip that iteration.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for people in ages:
    if people < 21:
        continue
    print(people)


# Example shows that while the "student_in_poetry" is less than 6 members long, we used .pop() to remove a student from
# "all_students" and assign that one student during the iteration to temp variable "student". From there we .append
# that student variable to the "students_in_poetry" list.
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)
print(students_in_poetry)


# Example Nested Loops with for/in into a for/in, this lets us break up lists into sublist, and those sublists we can
# pull values out of to add to our variable "scoops_sold"
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
    print(location)
    for sale in location:
        scoops_sold += sale
print(scoops_sold)


# Example of List Comprehension, where we take one list, in this case heights, and create a new "variable" = [brackets]
# We iterate/index using "height for height", we check the previous list using "in heights", then we apply the logic
# we care about using "if height > 161". Makes a list on the fly.
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)


# Example of List Comprehension, where we start creating new list "fahrenheit" = [brackets], the very first temp
# variable in bracket is what will end up posting to the new list so we can apply formatting to it, like an equation to
# convert the celsius value into fahrenheit.
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [(temp * 9/5 + 32) for temp in celsius]
print(fahrenheit)

# Example of List Comprehension, like above we are just applying a string related format instead of int related.
usernames = ["@coolguy35", "@kewldawg54", "@matchamom"]
messages = [name + " please follow me!" for name in usernames]
print(messages)


# Example exercise using Range, for/in loop, and list comprehension.
squares = []  # Assigns empty list to variable
single_digits = [i for i in range(10)]
print(single_digits)  # Prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for digit in single_digits:
    print(digit)  # Prints by line 0 through 9
    squares.append(digit ** 2)  # Appends the square value of digit to "squares" list
print(squares)  # Prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
cubes = [cube ** 3 for cube in single_digits]
print(cubes)  # Prints [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
