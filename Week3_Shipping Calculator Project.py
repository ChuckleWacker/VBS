# Calculate cost of ground shipping
def ground_shipping(weight):
  if weight <= 2.0:
    return (1.50 * weight) + 20.00
  elif weight > 2.0 and weight <= 6.0:
    return (3.00 * weight) + 20.00
  elif weight > 6.0 and weight <= 10.0:
    return (4.00 * weight) + 20.00
  elif weight > 10.0:
    return (4.75 * weight) + 20.00
# print(ground_shipping(41.5))

def drone_shipping(weight):
  if weight <= 2.0:
    return (4.50 * weight)
  elif weight > 2.0 and weight <= 6.0:
    return (9.00 * weight)
  elif weight > 6.0 and weight <= 10.0:
    return (12.00 * weight)
  elif weight > 10.0:
    return (14.25 * weight)
# print(drone_shipping(41.5))

premium = 125.00
# print(premium_shipping)

def cost(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if ground < drone and ground < premium:
    ship_type = "Ground"
    ship_cost = ground
  if drone < ground and drone < premium:
    ship_type = "Drone"
    ship_cost = drone
  if premium < ground and premium < drone:
    ship_type = "Premium"
    ship_cost = premium
  print("""The shipping method that is cheapest is {} Shipping.
           It will cost ${} to ship a package with a weight of {}.""".format(ship_type, ship_cost, weight))

cost((float(input("Enter weight here: "))))
