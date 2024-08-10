class Product:
    """
    Represents a product with a name, price, and optional discount price and quantity.

    Attributes:
        name (str): The name of the product.
        price (int or float): The price of the product.
        discount_price (int or float, optional): The discounted price of the product. Defaults to None.
        discount_quantity (int, optional): The quantity required to get the discounted price. Defaults to None.

    Raises:
        ValueError: If the product name is not a non-empty string, or if the price or discount price is not a non-negative number, or if the discount quantity is not a positive integer.
    """

    def __init__(self, name, price, discount_price=None, discount_quantity=None):
        if not isinstance(name, str) or not name:
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Product price must be a non-negative number.")
        if discount_price is not None and (not isinstance(discount_price, (int, float)) or discount_price < 0):
            raise ValueError("Discount price must be a non-negative number.")
        if discount_quantity is not None and (not isinstance(discount_quantity, int) or discount_quantity <= 0):
            raise ValueError("Discount quantity must be a positive integer.")

        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.discount_quantity = discount_quantity

    def get_price(self, quantity):
        """
        Calculates the total price of the product for a given quantity.

        Args:
            quantity (int): The quantity of the product.

        Returns:
            int or float: The total price of the product.

        Raises:
            Exception: If an error occurs while calculating the price.

        Example:
            >>> product = Product('A', 50, discount_price=130, discount_quantity=3)
            >>> product.get_price(4)
            180
        """
        try:
            if self.discount_quantity is not None and quantity >= self.discount_quantity:
                quo = quantity // self.discount_quantity
                rem = quantity % self.discount_quantity
                total_discounted_price = quo * self.discount_price + rem * self.price
                return total_discounted_price
            else:
                return self.price * quantity
        except Exception as e:
            print(f"Error calculating price for product '{self.name}': {e}")
            return 0


class Checkout:
    """
    Represents a checkout with a collection of products.

    Attributes:
        products (dict): A dictionary of products where the key is the product name and the value is a dictionary containing the product and quantity.
    """

    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        """
        Adds a product to the checkout.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product.

        Raises:
            Exception: If the product is not a Product instance or if the quantity is not a positive integer.

        Example:
            >>> checkout = Checkout()
            >>> product = Product('A', 50)
            >>> checkout.add_product(product, 2)
        """
        if not isinstance(product, Product):
            print(f"Invalid product added: {product}")
            return
        if not isinstance(quantity, int) or quantity <= 0:
            print(f"Invalid quantity '{quantity}' for product '{product.name}'. Quantity must be a positive integer.")
            return

        if product.name in self.products:
            self.products[product.name]['quantity'] += quantity
        else:
            self.products[product.name] = {'product': product, 'quantity': quantity}

    def calculate_total(self):
        """
        Calculates the total price of all products in the checkout.

        Returns:
            int or float: The total price of all products.

        Raises:
            Exception: If an error occurs while calculating the total.

        Example:
            >>> checkout = Checkout()
            >>> product = Product('A', 50)
            >>> checkout.add_product(product, 2)
            >>> checkout.calculate_total()
            100
        """
        total = 0
        try:
            for product_name, product_info in self.products.items():
                product = product_info['product']
                quantity = product_info['quantity']
                total += product.get_price(quantity)
        except Exception as e:
            print(f"Error calculating total: {e}")
        return total


class Supermarket:
    """
    Represents a supermarket with a collection of products.

    Attributes:
        products (dict): A dictionary of products where the key is the product name and the value is the product.
    """

    def __init__(self):
        self.products = {
            'A': Product('A', 50, discount_price=130, discount_quantity=3),
            'B': Product('B', 30, discount_price=45, discount_quantity=2),
            'C': Product('C', 20),
            'D': Product('D', 15)
        }

    def get_product(self, name):
        """
        Retrieves a product from the supermarket.

        Args:
            name (str): The name of the product.

        Returns:
            Product: The product if found, otherwise None.

        Raises:
            Exception: If the product is not found.

        Example:
            >>> supermarket = Supermarket()
            >>> supermarket.get_product('A')
            <Product 'A' at 0x...>
        """
        product = self.products.get(name)
        if product is None:
            print(f"Product '{name}' not found in the supermarket.")
            return None
        return product


def main():
    try:
        supermarket = Supermarket()
        checkout = Checkout()

        # Add products to checkout
        product_a = supermarket.get_product('A')
        if product_a:
            checkout.add_product(product_a, 3)
        product_b = supermarket.get_product('B')
        if product_b:
            checkout.add_product(product_b, 5)
        product_c = supermarket.get_product('C')
        if product_c:
            checkout.add_product(product_c, 1)
        product_d = supermarket.get_product('D')
        if product_d:
            checkout.add_product(product_d, 1)

        # Calculate total
        total = checkout.calculate_total()
        print(f'Total: {total}')

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()