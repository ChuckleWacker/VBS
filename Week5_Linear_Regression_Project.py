# Calculating errors between X and Y, an error is how many units away the points are.

# Function uses Quadratic Formula to calculate Y
def get_y(m, b, x):
    y = m * x + b
    return y


print(get_y(1,0,7) == 7)
print(get_y(5, 10, 3) == 25)


# Function calculates the distance between X and Y
def calculate_error(m, b, point):
    x_point, y_point = point
    y = m * x_point + b
    distance = abs(y - y_point)
    return distance


print((calculate_error(1, 0, (3, 3))))  # Y = X, so (3, 3) should lie on the point so #0 errors
print(calculate_error(1, 0, (3, 4)))  # Y = X, so (3, 4) should be 1 unit away so #1 errors
print(calculate_error(-1, 1, (3, 3)))  # Y = X, so (3, 3) so 3 = -1 * 3 + 1 or 3 = -2 which is a distance of 5 units


# Function calculates the cumulative distances of each set of points (x, y)
def calculate_all_errors(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error


datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print(calculate_all_errors(1, 0, datapoints))  # With the above list, cumulative errors should equal 6
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_errors(-1, 1, datapoints))  # With the above list, cumulative errors should equal 18


#########################################################
# Slopes and Intercepts

# Create lists from a range, using list comprehension
possible_ms = [m * 0.1 for m in range(-100, 100)]
print("MS List: " + str(possible_ms))
possible_bs = [b * 0.1 for b in range(-200, 200)]
print("BS List: " + str(possible_bs))

# Declare variables
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
best_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_errors(m, b, datapoints)
    if error < best_error:
        best_m = m
        best_b = b
        best_error = error

print(best_m, best_b, best_error)


#########################################################
# Model Prediction

print("The bounce heigh of a ball with a width of 6 will be: " + str(get_y(0.3, 1.7, 6)))
