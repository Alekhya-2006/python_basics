# Online Store (Combines Everything)

# Concepts: Constructor, Instance methods
# Class variable, Class method, Static method

class Product:

    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def product_info(self):
        print(f"Product = {self.name}"
              f"\nPrice = {self.price}")
    
    def update_price(self, new_price):
        self.price = new_price

    @classmethod    
    def product_count(cls):    
        return cls.total_products
    
    @staticmethod
    def calc_discount(price, discount):
       return price - (price * discount/100)

products = []

while True:
    print("\n1. Add Products")
    print("2. Display Products")
    print(("3. Update Price"))
    print("4. Total No Of Products")
    print("5. Calculate Discount")
    print("6. Exit")

    n = int(input("Choose Option (1-6): "))

    if n == 6:
        print("Successfully Exited")
        break

    if n > 0 and n <= 5:

        # Add products
        if n == 1:
            count = int(input("How many products do you want to add: "))

            for i in range(1, count+1):
                product_name = input(f'Name of the {i}th product: ')
                product_price = int(input("Price: "))

                product = Product(product_name, product_price)
                products.append(product)

            print("Added Successfully")

        # Display Products
        elif n == 2:
            if len(products) == 0:
                print("No Products Found")

            else:    
                for product in products:
                    product.product_info()

        # Update price
        elif n == 3:
            name = input("Enter name of the product: ")
            found = False

            for product in products:

                if product.name == name:
                    price = int(input("Enter new price: "))
                    product.update_price(price)
                    
                    found = True
                    print("Price Successfully Updated")

            if not found:
                print("Product Not Found")

        # Total No.Of Products
        elif n == 4:
            print(Product.product_count())
        
        # Calculate Discount
        else:
            price = int(input("Enter the price of the Product: "))
            discount = int(input("Enter Discount(in %): "))

            print(f"Discounted Price =", Product.calc_discount(price, discount))
