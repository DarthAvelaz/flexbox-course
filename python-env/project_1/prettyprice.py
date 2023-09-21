# pretty_price(3.20, 99) > 3.99
# pretty_price(3.20, 0.99) > 3.99

def pretty_price(gross_price, extension):
    return int(gross_price) + extension

print(pretty_price(2.50, 0.95))