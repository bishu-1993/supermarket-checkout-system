# Supermarket Checkout System
=============================

This is a Python implementation of a supermarket checkout system. The system allows customers to add products to their cart and calculates the total price based on the product prices and any applicable discounts.

## Features
-----------

* Product class with attributes for name, price, discount price, and discount quantity
* Checkout class with methods for adding products and calculating the total price
* Supermarket class with a dictionary of products
* Main script that demonstrates the usage of the system

## How to Run
-------------

1. Install Python 3.9 or later
2. Run the `main.py` script using Python: `python main.py`
3. The script will calculate the total price of the products in the checkout and print the result

## Dockerization
--------------

To run the script using Docker, follow these steps:

1. Build the Docker image: `docker build -t supermarket-app .`
2. Run the Docker container: `docker run -it supermarket-app`

## Notes
-----

* This implementation assumes a simple discount system where the discount price is applied when the quantity meets or exceeds the discount quantity.
* The system does not handle errors or exceptions extensively. You may want to add additional error handling and logging mechanisms in a production environment.

## Author
-------

Bishwajeet Kumar
