class Product:
    def __init__(self, product_id, name, spider_type, price, sex, image_url):
        """
        Represents a product in the ecommerce store.
        """
        self.product_id = product_id
        self.name = name
        self.spider_type = spider_type
        self.price = price
        self.sex = sex  # e.g., "acoustic", "electric", "bass"
        self.imageUrl = image_url



    def __repr__(self):
        return f"Product({self.name}, {self.spider_type}, ${self.price})"


class User:
    def __init__(self, user_id, username, email, password,user_type="customer"):
        """
        Represents a user in the ecommerce system.
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type  # "admin" or "customer"

    def is_admin(self):
        """Checks if the user is an admin."""
        return self.user_type == "admin"

    def __repr__(self):
        return f"User({self.username}, {self.email}, Type: {self.user_type})"


class LineItem:
    def __init__(self, product, quantity):
        """
        Represents an item in a shopping basket or order.
        """
        if not isinstance(product, Product):
            raise ValueError("LineItem must reference a Product.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __repr__(self):
        return f"LineItem(Product: {self.product.name}, Quantity: {self.quantity}, Total: ${self.total_price:.2f})"


class Basket:
    def __init__(self):
        """
        Represents a user's shopping basket.
        """
        self.items = []

    def add_item(self, product, quantity):
        """Adds an item to the basket."""
        self.items.append(LineItem(product, quantity))

    def remove_item(self, product_id):
        """Removes an item from the basket."""
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def calculate_total(self):
        """Calculates the total price of items in the basket."""
        return sum(item.total_price for item in self.items)

    def get_number_of_items(self):
        return len(self.items)

    def __repr__(self):
        return f"Basket({self.items})"


class Transaction:
    def __init__(self, transaction_id, user, basket):
        """
        Represents a completed transaction.
        """
        if not isinstance(user, User):
            raise ValueError("Transaction must reference a User.")
        if not isinstance(basket, Basket):
            raise ValueError("Transaction must reference a Basket.")
        self.transaction_id = transaction_id
        self.user = user
        self.basket = basket
        self.total_amount = basket.calculate_total()



    def __repr__(self):
        return f"Transaction(ID: {self.transaction_id}, User: {self.user.username}, Total: ${self.total_amount:.2f})"

def main():
    # Step 1: Create sample products
    product1 = Product(1, "Huntsman", "Common", 59.99, "Male", "huntsman.jpg")
    product2 = Product(2, "Wolf Spider", "Koch's Wolf Spider", 149.99, "Female", "wolf.jpg")


    # Step 2: Create a user
    customer = User(101, "john_doe", "john@example.com", "customer")

    # Step 3: Create a basket and add products
    basket = Basket()
    print("Adding items to the basket...")
    basket.add_item(product1, 2)
    basket.add_item(product2, 1)  #


    # Step 4: Display basket contents and total
    print("\nBasket contents:")
    for item in basket.items:
        print(item)
    print(f"Total Price: ${basket.calculate_total():.2f}")

    # Step 5: Create a transaction
    transaction = Transaction(1001, customer, basket)

    # Step 6: Display transaction details
    print("\nTransaction details:")
    print(transaction)




# Call the main function
if __name__ == "__main__":
    main()