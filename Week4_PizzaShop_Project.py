# PizzaShop starts creating a variable to track a list of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Creates a variable to track a list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Creates a variable to track the amount of pizza types offered = 7
num_pizzas = len(toppings)

# Print that we sell 7 types of pizzas
print("We sell {} different kinds of pizza!".format(num_pizzas))

# Creates a variable that creates a new list, using zip, that combines the lists "toppings" and "prices"
pizzas = list(zip(prices, toppings))
print(pizzas)  # Sanity check that the list displays correctly

# Sorts the new "pizzas" list so that the prices go from cheapest to most expensive
pizzas.sort()
print(pizzas)  # Sanity check that the list sorted correctly

# Creates a new variable that stores the cheapest pizza found in the "pizzas" list
cheapest_pizza = pizzas[0]
print(cheapest_pizza)  # Sanity check that the variable stored "cheese"

# Creates a new variable that stores the most expensive pizza found in the "pizzas" list
priciest_pizza = pizzas[-1]
print(priciest_pizza)  # Sanity check that the variable stored "anchovies"

# Creates a new variable that stores the three cheapest pizzas's found in the "pizzas" list
three_cheapest = pizzas[0:3]
print(three_cheapest)  # Sanity check that the variable stored "cheese, mushroom, olives"

# Creates a new variable that stores the number of $2 dollar pizzas, based on the price's list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)  # Sanity check that the variable stored "3" pizzas sold at $2
