# Project Title: Demo: Creation of an Insurance Management Portal using Python for Policyholder, Product, Payment and Report Management

# Created by:  Victor Kadiri

# Date Created: 22nd March 2025

# The Actual Analysis Begins in line 112

# Purpose: 
# The objective of the series of python scripts below is to create and manage insurance information such as Policyholder details, Product details, Payment details and report generation while ensuring appropriate error and file handling.
# The code uses a menu-driven approach to achieve its purpose. 
# It allows users to centrally manage policyholders, products, and payments modules separately by calling individual scripts within the main script. 
# Each module records are appended to a dictionary and stored as a json file in the corresponding output folder
# The Reports module allows users to view and save product, payment and policyholder details including applying filters such as paid, pending, active, suspended statuses to a physical file.
# The script utilizes series of python classes, methods, functions, libraries and syntax to address its objectives.

# Desired Output: The final output (generated report) would be written to a physical text file.

# Datasets used: No external datasets was used for this analysis

# Scripts Required: 
# 1. class_policy_holder_mgt.py
# 2. class_product_mgt.py
# 3. class_payment_mgt.py
# 4. policy_holder_demo.py

# Tools and Installations Required:
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher

# Procedures Performed:
# Step 1: Launch the VS Code application
# Step 2: Download the output and script folders from the GIT repository and place them in your desired folder location
# Step 3: Locate and open all the script source files (1. class_policy_holder_mgt.py, 2. class_product_mgt.py, 3. class_payment_mgt.py and 4. policy_holder_demo.py) using VS code
# Step 4a: Update output and scripts file paths within each script ensuring they align with your saved file paths in step 2.
# Step 4b: Save all script files leaving only the script file (policy_holder_demo.py) open
# Step 5: Locate and Click the "Run" button on the script file (policy_holder_demo.py)
# This will return a list of modules within the insurance management portal as shown below
#    --- Insurance Management Portal ---
#      P - Policyholder Management
#      R - Product Management
#      M - Payment Management
#      V - Reports
#      Q - Quit

# Step 6: Within the Insurance Management Portal, Type "P" to create or manage policyholder personal details. This will return a list of menu shown below.
#      i. R - Register a new policyholder
#     ii. P - Suspend a policyholder
#    iii. U - Update policyholder details
#    iv.  A - Reactivate a policyholder
#    v.   D - Display all policyholders
#    vi.  F - Find a policyholder
#    vii. S - Save policyholder data
#   viii. Q - Quit
# a. Then select any of the option above to create or update policy holder information.
# Once completed, type 'S' to save the data.
# Then type "Q" to return back to the Insurance Management Portal.


# Step 7: Within the Insurance Management Portal, Type "R" to create or manage product details. This will return a list of menu shown below.
#     i.     C - Create a new product
#    ii.     U - Update a product
#    iii.    P - Suspend a product
#    iv.     A - Reactivate a product
#     v.     D - Display all products
#    vi.     F - Find a product
#    vii.    S - Save product data
#    viii.   Q - Quit
# a. Then select any of the option above to create or update product information.
# Once completed, type 'S' to save the data.
# Then type "Q" to return back to the Insurance Management Portal.


# Step 8: Within the Insurance Management Portal, Type "M" to create or manage payment details. This will return a list of menu shown below.
#     i.     C - Create a new payment
#    ii.     P - Process a payment
#    iii.    R - Send a payment reminder
#    iv.     L - Apply a penalty to a payment
#     v.     D - Display all payments
#    vi.     F - Find a payment
#    vii.    S - Save payment data
#    viii.   Q - Quit
# a. Then select any of the option above to create, update, send payment reminders, apply penalty to a payment  payment information.
# Once completed, type 'S' to save the data 
# Then type "Q" to return back to the Insurance Management Portal.


# Step 9: Within the Insurance Management Portal, Type "V" to generate reports. This will return a list of menu shown below.
# ---- Report Module ------
#   1 - View all details
#   2 - View details by Policyholder ID
#   3 - View details by Product ID
#   4 - View details by Payment ID
#   5 - View policyholders with payment status and outstanding balance
# a. Then select any of the option above to generate the relevant reports.
# Once completed, type "Q" to return back to the Insurance Management Portal.

# Step 10: To generate reports of policyholders who have paid for one of the products and display their account details:
# a.  Type '5' within the Report module. This will return a list of menu shown below.
# --- Policyholders with Payment Status and Outstanding Balance ---
# 1 - All Payments
# 2 - Paid Payments
# 3 - Pending Payments
# 4 - Filter by Product
# 5 - Back to Reports Menu
# b. Then Type '2' within the 'Policyholders with Payment Status and Outstanding Balance' sub module to view the policyholders who have paid for one of the products and display their account details.
# c. Then type 'Y' when prompted to save the file. This will save the report as a txt outfile file.

# Note: 
# 1. You can view the intermittent outputs on the terminal panes 

# 2. Refer to the individual scripts for a detailed step by step procedures performed to achieve the development of an Insurance Management Portal using Python for creation and management of Policyholder details, Product details, Payment details and Report including error and file handling procedures.

#------------------------------------------------------------------------------------------
# ----------------------- The Actual Analysis Begins Here ---------------------------------

# The entire script below integrates the Policyholder, Product, and Payment Management classes into a menu-driven system.

# Step 1: This code imports the required modules for the analysis
import os
import json
import subprocess

# Step 2: This is a part where the user sets the desired output paths
# a. Set your output folder path (Remember to Change this to your desired output folder path)
output_folder_path = r"C:\Users\User\Downloads\BAN6420\Assignment_3\output"
# The script below creates this output folder path if it does not exist on your PC. This will prevent an error from occuring.
os.makedirs(output_folder_path, exist_ok=True)
# This line of code defines the output file paths
output_file_path = os.path.join(output_folder_path, "Policy_holder_details.txt")

# b. Set your script folder path (Remember to Change this to your desired script folder path)
script_folder_path = r"C:\Users\User\Downloads\BAN6420\Assignment_3\script"
# The script below creates this script folder path if it does not exist on your PC. This will prevent an error from occuring.
os.makedirs(script_folder_path, exist_ok=True)

# Step 3: Define paths for input JSON files
payment_data_path = os.path.join(output_folder_path, "payment_data.json")
product_data_path = os.path.join(output_folder_path, "product_data.json")
policyholder_data_path = os.path.join(output_folder_path, "policyholder_data.json")

# Step 4: Load data from JSON files
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        print(f"Error: File '{file_path}' not found.")
        return []

# Step 5: Link datasets and generate full account details
def link_datasets(policyholders, products, payments):
    linked_data = []
    for payment in payments:
        policyholder = next((ph for ph in policyholders if ph["policyholder_id"] == payment["policyholder_id"]), None)
        product = next((p for p in products if p["product_id"] == payment["product_id"]), None)

        if policyholder and product:
            linked_data.append({
                "policyholder_id": policyholder["policyholder_id"],
                "name": policyholder["name"],
                "email": policyholder["email"],
                "phone": policyholder["phone"],
                "policyholder_status": policyholder["status"],
                "product_id": product["product_id"],
                "product_name": product["name"],
                "product_price": product["price"],
                "product_status": product["status"],
                "payment_id": payment["payment_id"],
                "amount": payment["amount"],
                "due_date": payment["due_date"],
                "payment_status": payment["status"]
            })
    return linked_data

# Step 6: This code then creates a function to display and save details to a text file if requested
def display_and_save_details(linked_data, filter_by=None, filter_value=None):
    output = ""
    for entry in linked_data:
        if filter_by and entry[filter_by] != filter_value:
            continue

        output += f"Policyholder Details:\n"
        output += f"ID: {entry['policyholder_id']}\n"
        output += f"Name: {entry['name']}\n"
        output += f"Email: {entry['email']}\n"
        output += f"Phone: {entry['phone']}\n"
        output += f"Policyholder Status: {entry['policyholder_status']}\n"

        output += f"\nProduct Details:\n"
        output += f"ID: {entry['product_id']}\n"
        output += f"Name: {entry['product_name']}\n"
        output += f"Price: ${entry['product_price']}\n"
        output += f"Product Status: {entry['product_status']}\n"

        output += f"\nPayment Details:\n"
        output += f"Payment ID: {entry['payment_id']}\n"
        output += f"Amount: ${entry['amount']}\n"
        output += f"Due Date: {entry['due_date']}\n"
        output += f"Payment Status: {entry['payment_status']}\n"

        output += "-" * 50 + "\n"

    # This code displays the output
    print(output)

    # Ask the user if they want to save the output to a file
    save_choice = input("Do you want to save this report to a file? (Y/N): ").upper()
    if save_choice == "Y":
        with open(output_file_path, "w") as file:
            file.write(output)
        print(f"Output saved to '{output_file_path}'.")
    else:
        print("Output not saved.")

# Step 7: The sets of code below are used to demonstrate the functionality of the consolidated and integrated classes within policy holder management system.

# a. This is the main method used to initialize the entire code to demonstrate its functionality.
def main():
    # Load data from JSON files
    policyholders = load_data(policyholder_data_path)
    products = load_data(product_data_path)
    payments = load_data(payment_data_path)

    # Link datasets
    linked_data = link_datasets(policyholders, products, payments)

    # b. The code below provides a menu interface using a loop operation to allow the user to select the target task. The user can select from a range of options such as managing policyholders, managing products, managing payments, viewing reports, or quitting the program. The user then responds with the corresponding letter via the input function "choice" which is converted to uppercase to prevent errors.
    while True:
        print("\n--- Insurance Management Portal ---")
        print("P - Policyholder Management")
        print("R - Product Management")
        print("M - Payment Management")
        print("V - Reports")
        print("Q - Quit")
        choice = input("Enter your choice (P/R/M/V/Q): ").upper()

        # c. The code below implements one of the choices in 5b. It returns a message to manage policyholders, products, payments, or view reports.

        # c. i. This choice is for managing policyholders.
        if choice == "P":
            print("\n--- Policyholder Management ---")
            subprocess.run(["python", os.path.join(script_folder_path, "class_policy_holder_mgt.py")])

        # c. ii. This choice is for managing products.
        elif choice == "R":
            print("\n--- Product Management ---")
            subprocess.run(["python", os.path.join(script_folder_path, "class_product_mgt.py")])

        # c. iii. This choice is for managing payments.
        elif choice == "M":
            print("\n--- Payment Management ---")
            subprocess.run(["python", os.path.join(script_folder_path, "class_payment_mgt.py")])

        # c. iv. This choice is for viewing reports.
        elif choice == "V":
            while True:
                print("\n--- Reports ---")
                print("1 - View all details")
                print("2 - View details by Policyholder ID")
                print("3 - View details by Product ID")
                print("4 - View details by Payment ID")
                print("5 - View policyholders with payment status and outstanding balance")
                print("6 - Back to Main Menu")
                sub_choice = input("Enter your choice (1/2/3/4/5/6): ")

                if sub_choice == "1":
                    print("\n--- All Details ---")
                    display_and_save_details(linked_data)

                elif sub_choice == "2":
                    policyholder_id = input("Enter Policyholder ID: ").strip()
                    print(f"\n--- Details for Policyholder ID: {policyholder_id} ---")
                    display_and_save_details(linked_data, filter_by="policyholder_id", filter_value=policyholder_id)

                elif sub_choice == "3":
                    product_id = input("Enter Product ID: ").strip()
                    print(f"\n--- Details for Product ID: {product_id} ---")
                    display_and_save_details(linked_data, filter_by="product_id", filter_value=product_id)

                elif sub_choice == "4":
                    payment_id = input("Enter Payment ID: ").strip()
                    print(f"\n--- Details for Payment ID: {payment_id} ---")
                    display_and_save_details(linked_data, filter_by="payment_id", filter_value=payment_id)

                elif sub_choice == "5":
                    while True:
                        print("\n--- Policyholders with Payment Status and Outstanding Balance ---")
                        print("1 - All Payments")
                        print("2 - Paid Payments")
                        print("3 - Pending Payments")
                        print("4 - Filter by Product")
                        print("5 - Back to Reports Menu")
                        payment_filter_choice = input("Enter your choice (1/2/3/4/5): ")

                        if payment_filter_choice == "1":
                            print("\n--- All Payments ---")
                            display_and_save_details(linked_data)

                        elif payment_filter_choice == "2":
                            print("\n--- Paid Payments ---")
                            paid_data = [entry for entry in linked_data if entry["payment_status"] == "paid"]
                            display_and_save_details(paid_data)

                        elif payment_filter_choice == "3":
                            print("\n--- Pending Payments ---")
                            pending_data = [entry for entry in linked_data if entry["payment_status"] == "pending"]
                            display_and_save_details(pending_data)

                        elif payment_filter_choice == "4":
                            # Display available products as a dropdown
                            products = load_data(product_data_path)
                            if not products:
                                print("Error: No products found.")
                                continue

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
                                    print(f"\n--- Details for Product ID: {product_id} ---")
                                    product_data = [entry for entry in linked_data if entry["product_id"] == product_id]
                                    display_and_save_details(product_data)
                                else:
                                    print("Error: Invalid product selection. Please enter a valid number.")
                            except ValueError:
                                print("Error: Invalid input. Please enter a valid number.")

                        elif payment_filter_choice == "5":
                            break

                        else:
                            print("Invalid choice. Please try again.")

                elif sub_choice == "6":
                    break

                else:
                    print("Invalid choice. Please try again.")

        # c. v. This choice is for quitting the program.
        elif choice == "Q":
            print("Exiting the program. Goodbye!")
            break

        # d. This else statement helps to handle input errors from users by returning an "invalid choice" prompt.
        else:
            print("Invalid choice. Please try again.")


# e. This code is used to run the entire program
if __name__ == "__main__":
    main()