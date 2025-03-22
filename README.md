# README

# Project Title: Creation of an Insurance Management Portal using Python classes, libraries, functions and syntax to enable Policyholder, Product, Payment and Report Management

# Created by:  Victor Kadiri

# Date Created: 22nd March 2025

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



