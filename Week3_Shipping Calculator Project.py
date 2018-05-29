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

premium_shipping = 125.00
# print(premium_shipping)

def cost(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping:
      print("The shipping method that is cheapest is Ground Shipping.")
      print("It will cost ${} to ship a package with a weight of {} using this method.".format(ground_shipping(weight), weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_shipping:
      print("The shipping method that is cheapest is Drone Shipping.")
      print("It will cost ${} to ship a package with a weight of {} using this method.".format(drone_shipping(weight), weight))
  else:
      print("The shipping method that is cheapest is Premium Shipping.")
      print("It will cost ${} to ship a package with a weight of {} using this method.".format(125.00, weight))

# cost(4.8)
# cost(41.5)
cost((float(input("Enter weight here: "))))
