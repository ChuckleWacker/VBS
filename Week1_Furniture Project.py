# FURNITURE PROJECT WEEK 1

# Lovely Loveseat Description & Price
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

# Stylish Settee Description & Price
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50

# Luxurious Lamp Description & Price
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15

# Sales Tax is 8.8%
sales_tax = .088

# First Customer
customer_one_total = 0  # Starting Purchase
customer_one_itemization = ""  # Starting Itemization
customer_one_total = lovely_loveseat_price  # Love Seat Price
customer_one_itemization = lovely_loveseat_description  # Love Seat Item
customer_one_total += luxurious_lamp_price  # Luxurious Lamp Price
customer_one_itemization += " " + luxurious_lamp_description  # Luxurious Lamp Item
customer_one_tax = customer_one_total * sales_tax  # Total Tax Calculation
customer_one_total += customer_one_tax  # Ending Purchase
# First Customer Receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

# Second Customer
customer_two_total = 0  # Starting Purchase
customer_two_itemization = ""  # Starting Itemization
customer_two_total = stylish_settee_price  # Love Seat Price
customer_two_itemization = stylish_settee_description  # Love Seat Item
customer_two_total += luxurious_lamp_price  # Luxurious Lamp Price
customer_two_itemization += " " + luxurious_lamp_description  # Luxurious Lamp Item
customer_two_tax = customer_two_total * sales_tax  # Total Tax Calculation
customer_two_total += customer_two_tax  # Ending Purchase
# Second Customer Receipt
print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)
