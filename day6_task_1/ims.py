class ProductManager:
    product_id_counter = 0
    product_list = []

    @classmethod
    def generate_product_id(cls):
        cls.product_id_counter += 1
        return cls.product_id_counter

    @classmethod
    def get_all_products(cls):
        return cls.product_list

    def __init__(self, name, price, stock, category):
        self.id = self.generate_product_id()
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def add_product(self):
        self.get_all_products().append({'id': self.id, 'name': self.name, 'price': self.price,
                                        'stock': self.stock, 'category': self.category})

    def display_all_products(self):
        products_exist = False
        for product in self.get_all_products():
            print("ID:", product['id'], "Name:", product['name'], "Price:", product['price'],
                  "Stock:", product['stock'], "Category:", product['category'])
            products_exist = True

        if not products_exist:
            print("No products found")

    def generate_stock_report(self):
        try:
            low_stock_found = False
            for product in self.get_all_products():
                if product['stock'] < 10:
                    print("ID:", product['id'], "Name:", product['name'], "Price:", product['price'],
                          "Stock:", product['stock'], "Category:", product['category'])
                    low_stock_found = True

            if low_stock_found:
                print("Products with low stock")

            if not low_stock_found:
                print("No products with stock less than 10 available")
        except Exception as e:
            print(e)

    def update_product_info(self):
        try:
            product_id = int(input("Enter the ID of the product:"))
            product_found = False
            for product in self.get_all_products():
                if product['id'] == product_id:
                    print("Product Name:", product['name'])
                    new_price = float(input('Enter new price:'))
                    new_stock = int(input('Enter new stock:'))
                    new_category = input("Enter the new category of the product:")
                    product['price'] = new_price
                    product['stock'] = new_stock
                    product['category'] = new_category
                    product_found = True

            if not product_found:
                print("Product ID not found")
        except Exception as e:
            print(e)

    def remove_product(self):
        try:
            product_id = int(input("Enter the ID of the product to remove:"))
            for product in self.get_all_products():
                if product['id'] == product_id:
                    self.get_all_products().remove(product)
                    print(self.get_all_products())
                    product_found = True

            if not product_found:
                print("Product ID not found")

        except Exception as e:
            print(e)

class ElectronicInventory(ProductManager):
    def __init__(self, name, price, stock, category):
        super().__init__(name, price, stock, category)


exit_flag = 0

while exit_flag == 0:

    def exit_program():
        choice = input("-Are you sure you want to exit? (Y/N)")
        if choice.lower() == 'y':
            print("-Thank you!")
            return 1

    print("---- Inventory Management System ----")
    print("add -> Add product")
    print("view -> View all products")
    print("report -> Generate stock report")
    print("update -> Update product information")
    print("remove -> Remove product")
    print("exit -> Exit")

    user_choice = input("Enter your choice:")

    if user_choice.lower() == 'add':
        try:
            product_name = input('Enter the name of the product:')
            product_price = float(input("Enter the price of the product:"))
            product_stock = int(input("Enter the stock of the product: "))
            product_category = input("Enter the category of the product: ")
            product_data = ElectronicInventory(product_name, product_price, product_stock, product_category)
            product_data.add_product()
            print(id(product_data))
            print(ElectronicInventory.product_list)
        except Exception as e:
            print(e)

    elif user_choice.lower() == 'view':
        product_data.display_all_products()
        print(id(product_data))
    elif user_choice.lower() == 'report':
        product_data.generate_stock_report()
    elif user_choice.lower() == 'update':
        product_data.update_product_info()
    elif user_choice.lower() == 'remove':
        product_data.remove_product()

    elif user_choice.lower() == 'exit':
        exit_flag = exit_program()
    else:
        print("Please choose a valid option")
