# ----Project Title: Creating and Implementing a Class for Payment Management Using Python----------
# -------------------------------------------------------------------------------------------------------
# Note: The actual script run starts from line 32 of this python notebook.

# Created by:  Victor Kadiri
# Date Created: 22nd March 2025

# Purpose: This python script is created to perform class creation including implementing methods for payment processing, sending reminders, and applying penalties. It will also consider error handling procedures using Python. The script utilizes series of function, libraries and syntax to address its objectives.

# Desired Output: The final output of the python model will be tested by running and verifying that it aligns to objectives described above.

# Datasets used: No external datasets was used for this analysis

# Scripts Required: 
# a. class_payment_mgt.py
# b. class_product_mgt.py (for loading product data)

# Tools and Installations Required:
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher

# Procedures Performed:
# 1: Launch the VS Code application
# 2: Create two folders( i."output", ii. "scripts") in your desired location 
# 3: Download the script source file (a.class_payment_mgt.py) from the GIT repos into the "script" folder
# 4: Locate and open the script source file (a.class_payment_mgt.py) using VS code
# 5: Locate and Click the "Run" button on the script file (a.class_payment_mgt.py)
# 6: Explore the functionality and input functions
# 7: View the outputs on the terminal panes.
#------------------------------------------------------------------------------------------

# ----------------------- The Actual Analysis Begins Here ---------------------------------

# The entire script below creates a payment management class and implements methods for payment processing, sending reminders, and applying penalties.

# Step 1: Import the required modules
import os
import json

# Step 2: Define the paths for input and output
output_folder_path = input(r"Enter the path for the output folder (e.g., C:\Users\User\Downloads\BAN6420\Assignment_3\output): ")
product_data_path = os.path.join(output_folder_path, "product_data.json")
payment_data_path = os.path.join(output_folder_path, "payment_data.json")

# Step 3a: Load product data from the saved output of class_product_mgt.py
def load_product_data():
    if os.path.exists(product_data_path):
        with open(product_data_path, "r") as file:
            return json.load(file)
    else:
        print("No product data found. Please create products first.")
        return []

# Step 3b: Load Payment data from the saved output
def load_payment_data():
    if os.path.exists(payment_data_path):
        with open(payment_data_path, "r") as file:
            return json.load(file)
    else:
        print("No payment data found. Starting with an empty list.")
        return []
    
# Step 4: Save payment data to the specified output path
def save_payment_data(payments):
    # Convert payment objects to a dictionary format
    payment_list = []
    for payment in payments:
        payment_list.append({
            "payment_id": payment.payment_id,
            "policyholder_id": payment.policyholder_id,
            "product_id": payment.product_id,
            "amount": payment.amount,
            "due_date": payment.due_date,
            "status": payment.status
        })

    # Save the payment data to the JSON file
    with open(payment_data_path, "w") as file:
        json.dump(payment_list, file, indent=4)
    print(f"Payment data saved to '{payment_data_path}'.")


# Step 5: The script below creates a class for payment management
class PaymentManagement:

    # a. The code below is used to initialize a payment object with details such as payment_id, policyholder_id, product_id, amount, due_date, and the default status as "pending".
    def __init__(self, payment_id, policyholder_id, product_id, amount, due_date):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.due_date = due_date
        self.status = "pending"  # Default status is "pending"

    # b. The code below creates a method to process a payment. If initiated, the payment status will change from "pending" to "paid". It also implements error checks to identify if the payment is already processed. It either returns a message stating that the payment has now been processed or is already processed.
    def process_payment(self):
        if self.status == "pending":
            self.status = "paid"
            print(f"Payment {self.payment_id} (Policyholder ID: {self.policyholder_id}) has been processed.")
        else:
            print(f"Payment {self.payment_id} is already processed.")

    # c. The code below creates a method to send a payment reminder. If initiated, it checks if the payment is still pending. If the payment is pending, it sends a reminder. Otherwise, it notifies that no reminder is needed.
    def send_reminder(self):
        if self.status == "pending":
            print(f"Reminder sent for Payment {self.payment_id} (Policyholder ID: {self.policyholder_id}). Amount due: ${self.amount} by {self.due_date}.")
        else:
            print(f"No reminder needed. Payment {self.payment_id} is already processed.")

    # d. The code below creates a method to apply a penalty to a payment. If initiated, it checks if the payment is still pending. If the payment is pending, it applies a penalty to the amount due. Otherwise, it notifies that no penalty is applied.
    def apply_penalty(self, penalty_amount):
        if self.status == "pending":
            self.amount += penalty_amount
            print(f"Penalty of ${penalty_amount} applied to Payment {self.payment_id}. New amount due: ${self.amount}.")
        else:
            print(f"No penalty applied. Payment {self.payment_id} is already processed.")

    # e. The code below creates a method to display payment details. It displays all the details of the payment in a readable format.
    def display_details(self):
        print(f"Payment Details:\nPayment ID: {self.payment_id}\nPolicyholder ID: {self.policyholder_id}\nProduct ID: {self.product_id}\nAmount: ${self.amount}\nDue Date: {self.due_date}\nStatus: {self.status}")


# Step 6: The sets of code below are used to demonstrate the functionality of the payment management class above

# a. This is the main method used to initialize the payment management code run to demonstrate its functionality.
def main():

    # b.(i) The code below initializes an empty list to store all payments.
    payments = []

    # b. (ii) 
    # The code below loads existing payment data from the JSON file
    existing_payments = load_payment_data()
    for payment_data in existing_payments:
        payment = PaymentManagement(
            payment_data["payment_id"],
            payment_data["policyholder_id"],
            payment_data["product_id"],
            payment_data["amount"],
            payment_data["due_date"]
        )
        payment.status = payment_data["status"]  # Set the payment status
        payments.append(payment)  # Add the existing payment to the list

    # c. The code below provides a menu interface using a loop operation to allow the user to select the target task. The user can select from a range of options such as creating a payment, processing a payment, sending a reminder, applying a penalty, displaying all payments, or searching for a payment. The user then responds with the corresponding letter via the input function "choice" which is converted to uppercase to prevent errors.
    while True:
        print("\n--- Payment Management Module ---")
        print("C - Create a new payment")
        print("P - Process a payment")
        print("R - Send a payment reminder")
        print("L - Apply a penalty to a payment")
        print("D - Display all payments")
        print("F - Find a payment")
        print("S - Save payment data")
        print("Q - Quit")
        choice = input("Enter your choice (C/P/R/L/D/F/S/Q): ").upper()

        # d. The code below implements one of the choices in 2c. It returns a message to create a new payment if it doesn't exist in the payment management system.

        # d. i. This choice is for the creation of a new payment.
        if choice == "C":
            print("\nCreate a New Payment")
            payment_id = input("Enter Payment ID: ")
            policyholder_id = input("Enter Policyholder ID: ")

            # Load product data
            products = load_product_data()
            if not products:
                print("Error: No products found. Please create products first.")
                continue  # Skip payment creation if no products exist

            # Display available products as a dropdown
            print("\nAvailable Products:")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. ID: {product['product_id']}, Name: {product['name']}, Price: ${product['price']}")

            # Allow the user to select a product by index
            product_choice = input("Enter the number of the product: ").strip()
            try:
                product_choice = int(product_choice)
                if 1 <= product_choice <= len(products):
                    selected_product = products[product_choice - 1]
                    product_id = selected_product["product_id"]
                    amount = float(input("Enter Amount: "))
                    due_date = input("Enter Due Date (YYYY-MM-DD): ")
                    payment = PaymentManagement(payment_id, policyholder_id, product_id, amount, due_date)
                    payments.append(payment)  # Add the new payment to the list
                    print(f"Payment {payment_id} (Policyholder ID: {policyholder_id}) has been created.")
                else:
                    print("Invalid product selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # d. ii. This choice is for processing a payment.
        elif choice == "P":
            payment_id = input("Enter Payment ID to process: ").strip()
            for payment in payments:
                if payment.payment_id == payment_id:
                    payment.process_payment()
                    break
            else:
                print("Payment not found.")

        # d. iii. This choice is for sending a payment reminder.
        elif choice == "R":
            payment_id = input("Enter Payment ID to send a reminder: ").strip()
            for payment in payments:
                if payment.payment_id == payment_id:
                    payment.send_reminder()
                    break
            else:
                print("Payment not found.")

        # d. iv. This choice is for applying a penalty to a payment.
        elif choice == "L":
            payment_id = input("Enter Payment ID to apply a penalty: ").strip()
            penalty_amount = float(input("Enter Penalty Amount: "))
            for payment in payments:
                if payment.payment_id == payment_id:
                    payment.apply_penalty(penalty_amount)
                    break
            else:
                print("Payment not found.")

        # d. v. This choice is for displaying all payments.
        elif choice == "D":
            if not payments:
                print("No payments found.")
            else:
                print("\n--- All Payments ---")
                for payment in payments:
                    payment.display_details()
                    print("-" * 30)

        # d. vi. This choice is for searching for a payment by Payment ID, Policyholder ID, or Product ID.
        elif choice == "F":
            search_term = input("Enter Payment ID, Policyholder ID, or Product ID to search: ").strip()
            found = False
            for payment in payments:
                if (search_term == payment.payment_id or
                    search_term == payment.policyholder_id or
                    search_term == payment.product_id):
                    payment.display_details()
                    found = True
            if not found:
                print("No matching payment found.")

        # d. vii. This choice is for saving payment data to a JSON file.
        elif choice == "S":
            save_payment_data(payments)

        # d. viii. This choice is for quitting the payment management menu interface.
        elif choice == "Q":
            print("Exiting the program. Goodbye!")
            break

        # e. This else statement helps to handle input errors from users by returning an "invalid choice" prompt.
        else:
            print("Invalid choice. Please try again.")


# f. This code is used to run the entire program
if __name__ == "__main__":
    main()