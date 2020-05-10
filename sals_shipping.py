def ground_shipping(weight):
  if weight <= 2.00:
    price_per_pound = 1.50
  elif weight <= 6.00:
    price_per_pound = 3.00
  elif weight <= 10.00:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return (price_per_pound * weight) + 20

print(ground_shipping(8.40))

premium_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2.00:
    price_per_pound = 4.50
  elif weight <= 6.00:
    price_per_pound = 9.00
  elif weight <= 10.00:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return (price_per_pound * weight)

print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_shipping
  if ground < drone and ground < premium:
    method = "ground"
    cost = ground
  elif drone < ground and drone < premium:
    method = "drone"
    cost = drone
  else:
    method = "premium"
    cost = premium
  print ("The cheapest way to ship " + str(weight) + " pound package is using %s shipping and it will cost $%.2f" %(method, cost) + ".")

cheapest_shipping(4.8)
cost = cheapest_shipping(41.5)
