# Save a string, pick a value from that string, in this case the D using index #0, print D
my_name = "Daniel"
first_initial = my_name[0]
print(first_initial)


# Slicing strings by their indices
first_name = "Daniel"
last_name = "Boggs"
new_account = first_name[:3]  # Slice first 3 characters
print(new_account)  # prints "Dan"
temp_password = last_name[1:4]  # Slice 2nd through 4th characters, middle slice
print(temp_password)  # prints "ogg" since there is no 6th character


# Create a function that takes the first three letters of two strings and combines them.
first_name = "Daniel"
last_name = "Boggs"

def account_generator(first_name, last_name):  # This function will take two variables and concatenates them
    return first_name[:3] + last_name[:3]
new_account = account_generator(first_name, last_name)
print(new_account)  # prints "DanBog"


# Function takes the last three letters of each name and concatenates them
first_name = "Daniel"
last_name = "Boggs"

def password_generator(first_name, last_name):
    #return first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]  # Using len() method
    return first_name[-3:] + last_name[-3:]  # Using negative indices
temp_password = password_generator(first_name, last_name)
print(temp_password)  # prints "ielggs"


# Slice using negative indices, opposed to above using len()
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2:-1]  # Find second to last character
final_word = company_motto[-4:]  # Find last four characters
print(second_to_last)
print(final_word)


# Example that you cannot update an index of a string, so you create a new variable/string with change and slicing
first_name = "Bob"
last_name = "Daily"
# first_name[0] = "R"  # Strings are immutable, cannot update
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)  # prints "Rob" instead of "Bob"


# Using \ to escape a character from triggering, in this case a quotes
# Password = "theycallme"crazy"91"  # This would cause an error as the quotations within the string aren't escaped
password = "theycallme\"crazy\"91"


# Two ways of determining length of a string
def get_length(word):
    counter = 0
    for letters in word:
        counter += 1
    return counter
print(get_length("Boggs"))

def get_length2(word):
    return len(word)
print(get_length2("Daniel"))


# Count the number of times a specific letter shows up, in this case "b"
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1
print(counter)  # prints 2


def letter_check(word, letter):
    for i in word:
        print(i)
        if i == letter:
            print("True")
            return True
    print("False")
    return False
letter_check("Daniel", "n")
letter_check("Daniel", "z")


# Function takes two strings, compares them index by index and adds matching letters to temp list, also makes sure
# temp list doesnt already have the letter using "and not letter in lst"
def common_letters(string_one, string_two):
    lst = []
    for letter in string_one:
        if letter in string_two and not letter in lst:
            lst.append(letter)
    return lst
print(common_letters("banana", "cream"))  # should pint "a" as this is the only common letter found


# Example of generating a username using splicing or commented section dives into a len() variant
def username_generator1(first_name, last_name):
    return first_name[:3] + last_name[:4]
#def username_generator(first_name, last_name):
#    if len(first_name) < 3:
#        user_name = first_name
#    else:
#        user_name = first_name[0:3]
#    if len(last_name) < 4:
#        user_name += last_name
#    else:
#        user_name += last_name[0:4]
#    return user_name
print(username_generator1("Daniel", "Boggs"))

# Example of generating a password using a slicing model vs an iterative model
def password_generator1(user_name):
    return user_name[-1:] + user_name[:-1]
#print(password_generator("BogDan"))
#def password_generator(user_name):
#    password = ""
#    for i in range(0, len(user_name)):
#        password += user_name[i - 1]
#    return password
print(password_generator1("BogDan"))


# Function to iterate through the length of a word, and select every other letter based on the index being even
def print_some_characters(word):
    for i in range(len(word)):
        if i % 2 == 0:
          print(word[i])
print(print_some_characters("watermelon"))