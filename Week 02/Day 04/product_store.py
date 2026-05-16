# Design and create an online store for Products(name, price)
# Track total products being created.
# Create a static method to calc discount on each product on a % parameter.

class Products:
    product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.product_count += 1

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        return final_price

p1 = Products("watch", 2000)
p2 = Products("Perfume", 5000)

print(f'Discounted price = {Products.calc_discount(p1.price, 10)}')
print(f'Total products = {Products.product_count}')