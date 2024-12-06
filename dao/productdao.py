from model.models import Product


class ProductDAO:
    def __init__(self):
        """
        Initializes the ProductDAO with a sample collection of products.
        """
        self.products = [
            Product(1, "Huntsman", "Common", 59.99, "Male", "huntsman.jpeg"),
            Product(2, "Wolf Spider", "Koch's Wolf Spider", 149.99, "Female", "wolf.jpeg"),
            Product(3, "Jumping Spider", "Phidippus clarus", 24.99, "male", "jumping.jpeg"),
            Product(4, "Brazilian Black Tarantula", "Grammostola pulchra", 99.99, "female", 'brazillian black.jpeg'),
            Product(5, "Greenbottle blue tarantula", "Terrestrial", 89.99, "male", 'greenbottle.jpeg'),
            Product(6, "Curly Hair Tarantula", "Tliltocatl albopilosus", 39.99, "male", 'curly.jpeg'),
            Product(7, "Common Garden Spider", "Hololena", 9.99, "female", 'common.jpeg'),
            Product(8, "Golden Silk Orb-Weaver Spider", "Trichonephila clavipes", 25.99, "female", 'golden.jpeg'),

        ]

    def getAllProducts(self):
        """
        Retrieves all products in the catalog.
        """
        return self.products

    def getProduct(self, product_id):
        """
        Retrieves a single product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The product with the given ID, or None if not found.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None  # Product not found


# Example usage of ProductDAO
def main_with_dao():
    product_dao = ProductDAO()

    print("All Products:")
    for product in product_dao.getAllProducts():
        print(product)

    print("\nFetching Product by ID (ID: 2):")
    product = product_dao.getProduct(2)
    if product:
        print(product)
    else:
        print("Product not found.")


if __name__ == "__main__":
    main_with_dao()
