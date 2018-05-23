train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


# Function converts fahrenheit to celsius temperature
def f_to_c(f_temp):
    c_temp = f_temp - 32 * 5/9
    return c_temp


# Testing function by plugging in 100 degrees fahrenheit, should output 37.7778 celsius
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)


# Function converts celsius to fahrenheit temperature
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp


# Testing function by plugging in 0 degrees celsius, should output 32.0 fahrenheit
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


# Function to calculate force
def get_force(mass, acceleration):
    return mass * acceleration


# Assigning variable train_force to equal function get_force with parameters train_mass & train_acceleration plugged in
train_force = get_force(train_mass, train_acceleration)


# Function to calculate energy
def get_energy(mass, c=3*10**8):
    return (mass * c) ^ 2


# Assigning variable bomb_energy to equal function get_energy with parameter bomb_mass plugged in
bomb_energy = get_energy(bomb_mass)


# Function to calculate work in Joules using force multiplied by distance
# Acquire force by calling get_force function within the get_work function
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance


# Assigning variable train_work to equal function get_work with parameters train_mass & train_acceleration
# which are used to pass to above subFunction get_force, and then parameter train_distance.
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
