# --Project Title: Creating and Implementing a Class for Product Management Using Python---
# -----------------------------------------------------------------------------------------
# Note: The actual script run starts from line 32 of this python notebook.

# Created by:  Victor Kadiri
# Date Created: 22nd March 2025

# Purpose: This python script is created to perform class creation including implementing methods for creating, updating, and removing/suspending policy products. It will also consider error handling procedures using Python. The script utilizes series of function, libraries and syntax to address its objectives.

# Desired Output: The final output of the python model will be tested by running and verifying that it aligns to objectives described above.

# Datasets used: No external datasets was used for this analysis

# Scripts Required: 
# a. class_product_mgt.py

# Tools and Installations Required:
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher

# Procedures Performed:
# 1: Launch the VS Code application
# 2: Create two folders( i."output", ii. "scripts") in your desired location 
# 3: Download the script source file (a.class_product_mgt.py) from the GIT repos into the "script" folder
# 4: Locate and open the script source file (a.class_product_mgt.py) using VS code
# 5: Locate and Click the "Run" button on the script file (a.class_product_mgt.py)
# 6: Explore the functionality and input functions
# 7: View the outputs on the terminal panes.
#------------------------------------------------------------------------------------------

# ----------------------- The Actual Analysis Begins Here ---------------------------------

# The entire script below creates a product management class and implements methods for creating, updating, and removing/suspending policy products.
# Step 1: Import the required modules
import os
import json

# Step 2: Define the paths for input and output
output_folder_path = input(r"Enter the path for the output folder (e.g., C:\Users\User\Downloads\BAN6420\Assignment_3\output): ")
product_data_path = os.path.join(output_folder_path, "product_data.json")

# Step 3: Load product data from the saved output
def load_product_data():
    if os.path.exists(product_data_path):
        with open(product_data_path, "r") as file:
            return json.load(file)
    else:
        print("No product data found. Starting with an empty list.")
        return []


# Step 4: Save product data to the specified output path
def save_product_data(products):
    # Convert product objects to a dictionary format
    product_list = []
    for product in products:
        product_list.append({
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "status": product.status
        })

    # Save the product data to the JSON file
    with open(product_data_path, "w") as file:
        json.dump(product_list, file, indent=4)
    print(f"Product data saved to '{product_data_path}'.")


# Step 5: The script below creates a class for product management
class ProductManagement:

    # a. The code below is used to initialize a product object with details such as product_id, name, price, and the default status as "active".
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = "active"  # Default status is "active"

    # b. The code below creates a method to update the product details. If initiated, product details such as name and price can be inputted and updated. It also implements error checks using data validation techniques(data types) to ensure that the right inputs are captured. It returns a message stating any updates made to the product record as well as display the full details for easy reference.
    def update_name(self, new_name):
        self.name = new_name
        print(f"Product name updated to: {self.name}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Product price updated to: ${self.price}")

    # c. The code below creates a method to suspend a product. If initiated, the product status will change from "active" to "suspended". It also implements error checks to identify if the product is already suspended. It either returns a message stating that the product has now been suspended or is already suspended.
    def suspend(self):
        if self.status == "active":
            self.status = "suspended"
            print(f"Product {self.name} (ID: {self.product_id}) has been suspended.")
        else:
            print(f"Product {self.name} is already suspended.")

    # d. The code below creates a method to reactivate a product. If initiated, the product status will change from "suspended" back to "active". It also implements error checks to identify if the product is already active. It either returns a message stating that the product has now been reactivated or is already active.
    def reactivate(self):
        if self.status == "suspended":
            self.status = "active"
            print(f"Product {self.name} (ID: {self.product_id}) has been reactivated.")
        else:
            print(f"Product {self.name} is already active.")

    # e. The code below creates a method to display product details. It displays all the details of the product in a readable format.
    def display_details(self):
        print(f"Product Details:\nID: {self.product_id}\nName: {self.name}\nPrice: ${self.price}\nStatus: {self.status}")


# Step 6: The sets of code below are used to demonstrate the functionality of the product management class above

# a. This is the main method used to initialize the product management code run to demonstrate its functionality.
def main():

    # b. The code below initializes an empty list to store all products.
    products = []

    # Load existing product data if available
    existing_products = load_product_data()
    for product_data in existing_products:
        product = ProductManagement(product_data["product_id"], product_data["name"], product_data["price"])
        product.status = product_data["status"]
        products.append(product)

    # c. The code below provides a menu interface using a loop operation to allow the user to select the target task. The user can select from a range of options such as creating a product, updating a product, suspending a product, reactivating a product, displaying all products, or searching for a product. The user then responds with the corresponding letter via the input function "choice" which is converted to uppercase to prevent errors.
    while True:
        print("\n--- Product Management Module ---")
        print("C - Create a new product")
        print("U - Update a product")
        print("P - Suspend a product")
        print("A - Reactivate a product")
        print("D - Display all products")
        print("F - Find a product")
        print("S - Save product data")
        print("Q - Quit")
        choice = input("Enter your choice (C/U/P/A/D/F/S/Q): ").upper()

        # d. The code below implements one of the choices in 2c. It returns a message to create a new product if it doesn't exist in the product management system.

        # d. i. This choice is for the creation of a new product.
        if choice == "C":
            print("\nCreate a New Product")
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            product = ProductManagement(product_id, name, price)
            products.append(product)  # Add the new product to the list
            print(f"Product {name} (ID: {product_id}) has been created.")
            save_product_data(products)  # Save the updated product list to JSON

        # d. ii. This choice is for updating a product.
        elif choice == "U":
            product_id = input("Enter Product ID to update: ").strip()
            for product in products:
                if product.product_id == product_id:
                    while True:
                        print("\nWhat would you like to update?")
                        print("1. Name")
                        print("2. Price")
                        print("3. Exit Update Menu")
                        update_choice = input("Enter your choice (1/2/3): ")

                        if update_choice == "1":
                            new_name = input("Enter new name: ")
                            product.update_name(new_name)
                        elif update_choice == "2":
                            new_price = float(input("Enter new price: "))
                            product.update_price(new_price)
                        elif update_choice == "3":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                        product.display_details()
                    save_product_data(products)  # Save the updated product list to JSON
                    break
            else:
                print("Product not found.")

        # d. iii. This choice is for suspending a product.
        elif choice == "P":
            product_id = input("Enter Product ID to suspend: ").strip()
            for product in products:
                if product.product_id == product_id:
                    product.suspend()
                    save_product_data(products)  # Save the updated product list to JSON
                    break
            else:
                print("Product not found.")

        # d. iv. This choice is for reactivating a product.
        elif choice == "A":
            product_id = input("Enter Product ID to reactivate: ").strip()
            for product in products:
                if product.product_id == product_id:
                    product.reactivate()
                    save_product_data(products)  # Save the updated product list to JSON
                    break
            else:
                print("Product not found.")

        # d. v. This choice is for displaying all products.
        elif choice == "D":
            if not products:
                print("No products found.")
            else:
                print("\n--- All Products ---")
                for product in products:
                    product.display_details()
                    print("-" * 30)

        # d. vi. This choice is for searching for a product by Product ID or Name.
        elif choice == "F":
            search_term = input("Enter Product ID or Name to search: ").strip()
            found = False
            for product in products:
                if search_term == product.product_id or search_term.lower() in product.name.lower():
                    product.display_details()
                    found = True
            if not found:
                print("No matching product found.")

        # d. vii. This choice is for saving product data to a JSON file.
        elif choice == "S":
            save_product_data(products)

        # d. viii. This choice is for quitting the product management menu interface.
        elif choice == "Q":
            print("Exiting the program. Goodbye!")
            break

        # e. This else statement helps to handle input errors from users by returning an "invalid choice" prompt.
        else:
            print("Invalid choice. Please try again.")


# f. This code is used to run the entire program
if __name__ == "__main__":
    main()