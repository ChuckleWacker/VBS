hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

# Calculate the total price of list "prices"
total_price = 0
for price in prices:
    total_price += price
print("Total Price: $" + str(total_price))

# Calculate the average price of list "total_price" by dividing with the length of list "prices"
average_price = total_price / len(prices)
print("Average Price: $" + str(average_price))

# Create a new list of prices that are reduced by $5
new_prices = [price - 5 for price in prices]
print("New Price List: " + str(new_prices))

# Calculate Total Revenue by iterating through lists "prices" and "last_week" to calculate earnings
total_revenue = 0
for i in range(0, len(hairstyles) - 1):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" + str(total_revenue))

# Calculate daily revenue average
average_revenue = total_revenue / 7
print("Average Revenue: $" + str(average_revenue))

# Create a new list of Hairstyles that cost less than $30 based on lists "hairstyles" and "new_prices"
cuts_under_30 = [hairstyles[i] for i in range(0, len(hairstyles) - 1) if new_prices[i] < 30]
print("Haircuts Under $30: {}".format(cuts_under_30))
