product_id = 123
sale_price = 14.99
tip_percentage = 1/5
new_product = 150

#print(sale_price + new_product)
#print(product_id + new_product)


#print('Addition')
#print(100 + 42)

#print('Subtraction')
#print(100 - 42)

#print('Division')
#print(100 / 42)
#print(100 / 38)

#print('Floor Division')
#print(100 // 42)
#print(100 // 38)

#print('Multiplication')
#print(100 * 42)

#print('Modulus')
#print(100 % 42)

#print('Exponents')
#print(100 ** 42)


#"""
#Please -> Parans ()
#Excuse -> Exponents **
#My -> Multiplication *
#Dear -> Division /
#Aunt -> Addition +
#ally -> Subtraction -

#8 + 2 * 5 - (9 + 2) ** 2
#8 + 2 * 5 - 11 ** 2
#8 + 2 * 5 - 121
#8 + 10 - 121
#-103
#"""

#calculation = 8 + 2 * 5 - (9 + 2) ** 2

#print(calculation)


total = 100

total = total + 10
total += 10
total -= 10
total *= 2
total /= 10
total //= 10
total **= 2
total %= 2

product_two = 120
product_three = 10

total += product_two
total += product_three

print(total)

from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451