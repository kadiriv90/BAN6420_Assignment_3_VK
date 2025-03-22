# ----Project Title: Creating a class for Policy holder management using Python----------
# -------------------------------------------------------------------------------------------------------
# Note: The actual script run starts from line 32 of this python notebook.

# Created by:  Victor Kadiri
# Date Created: 22nd March 2025

# Purpose: This python script is created to perform class creation including implementing methods to register, suspend, reactivate and update policyholder records. It will also consider error handling procedures using Python. The script utilizes series of function, libraries and syntax to address its objectives.

# Desired Output: The final output of the python model will be tested by running and verifying that it aligns to objectives described above.

# Datasets used: No external datasets was used for this analysis

# Scripts Required: 
# a. class_policy_holder_mgt.py

# Tools and Installations Required:
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher

# Procedures Performed:
# 1: Launch the VS Code application
# 2: Create two folders( i."output", ii. "scripts") in your desired location 
# 3: Download the script source file (a.class_policy_holder_mgt.py) from the GIT repos into the "script" folder
# 4: Locate and open the script source file (a.class_policy_holder_mgt.py) using VS code
# 5: Locate and Click the "Run" button on the script file (a.class_policy_holder_mgt.py)
# 6: Explore the functionality and input functions
# 7: View the outputs on the terminal panes.
#------------------------------------------------------------------------------------------

# ----------------------- The Actual Analysis Begins Here ---------------------------------

# The entire script below creates a policy holder class and implements methods to register, suspend, reactivate and update policyholder records.

# Step 1: Import the required modules
import os
import json

# Step 2: Define the paths for input and output
output_folder_path = r"C:\Users\User\Downloads\BAN6420\Assignment_3\output"
policyholder_data_path = os.path.join(output_folder_path, "policyholder_data.json")

# Step 3: Load policyholder data from the saved output
def load_policyholder_data():
    if os.path.exists(policyholder_data_path):
        with open(policyholder_data_path, "r") as file:
            return json.load(file)
    else:
        print("No policyholder data found. Starting with an empty list.")
        return []


# Step 4: Save policyholder data to the specified output path
def save_policyholder_data(policyholders):
    # Convert policyholder objects to a dictionary format
    policyholder_list = []
    for policyholder in policyholders:
        policyholder_list.append({
            "policyholder_id": policyholder.policyholder_id,
            "name": policyholder.name,
            "email": policyholder.email,
            "phone": policyholder.phone,
            "status": policyholder.status
        })

    # Save the policyholder data to the JSON file
    with open(policyholder_data_path, "w") as file:
        json.dump(policyholder_list, file, indent=4)
    print(f"Policyholder data saved to '{policyholder_data_path}'.")


# Step 5: The script below creates a class for all policy holders
class Policyholder:

    # a. The code below is used to initialize a policyholder object with details such as policyholder_id, name, email , phone number and the default status as active.
    def __init__(self, policyholder_id, name, email, phone):
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.phone = phone
        self.status = "active" 

    # b. The code below creates a method to allow the update of a policy holder details. If initiated, policy holder details such as name, email and phone number can be inputted and updated. It also implements error checks using data validation techniques(data types) to ensure that the right inputs are captured. It returns a message stating any updates made to a policy holder record as well as display the full details for easy reference.
    def update_name(self, new_name):
        self.name = new_name
        print(f"Policyholder name updated to: {self.name}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"Policyholder email updated to: {self.email}")

    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"Policyholder phone number updated to: {self.phone}")

    def display_details(self):
        print(f"Policyholder Details:\nID: {self.policyholder_id}\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nStatus: {self.status}")

    # c. The code below creates a method to allow the suspension of a policy holder. If initiated, the policy holder status will change from "active" to "suspended". It also implements error checks to identify if the policy holder is already suspended. It either returns a message stating that the policy holder has now been suspended or is already suspended.
    def suspend(self):
        if self.status == "active":
            self.status = "suspended"
            print(f"Policyholder {self.name} (ID: {self.policyholder_id}) has been suspended.")
        else:
            print(f"Policyholder {self.name} is already suspended.")

    # d. The code below creates a method to allow the reactivation of a policy holder. If initiated, the policy holder status will change from "suspended" back to "active". It also implements error checks to identify if the policy holder is already active. It either returns a message stating that the policy holder has now been reactivated or is already active.
    def reactivate(self):
        if self.status == "suspended":
            self.status = "active"
            print(f"Policyholder {self.name} (ID: {self.policyholder_id}) has been reactivated.")
        else:
            print(f"Policyholder {self.name} is already active.")


# e. The code below is used to register a new policy holder. If initiated, policy holder details such as name, email and phone number can be inputted and registered. It also implements error checks using data validation techniques(data types) to ensure that the right inputs are captured. It displays the full details of the newly registered policy holder for easy reference.
def register_policyholder(policyholders):
    print("\nRegister a New Policyholder")
    policyholder_id = input("Enter Policyholder ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    policyholder = Policyholder(policyholder_id, name, email, phone)
    policyholders.append(policyholder)  # Add the new policyholder to the list
    print(f"Policyholder {name} (ID: {policyholder_id}) has been registered.")
    save_policyholder_data(policyholders)  # Save the updated policyholder list to JSON


# f. The code below is used to display all registered policyholders.
def display_all_policyholders(policyholders):
    if not policyholders:
        print("No policyholders registered.")
    else:
        print("\n--- All Policyholders ---")
        for policyholder in policyholders:
            policyholder.display_details()
            print("-" * 30)


# g. The code below is used to search for a policyholder by ID, name, email, or phone.
def search_policyholder(policyholders):
    search_term = input("Enter Policyholder ID, Name, Email, or Phone to search: ").strip().lower()
    found = False

    for policyholder in policyholders:
        if (search_term == policyholder.policyholder_id.lower() or
            search_term in policyholder.name.lower() or
            search_term == policyholder.email.lower() or
            search_term == policyholder.phone.lower()):
            policyholder.display_details()
            found = True

    if not found:
        print("No matching policyholder found.")


# Step 6: The sets of code below are used to demonstrate the functionality of the policy holder class above

# a. This is the main method used to initialize the policy holder code run to demonstrate its functionality.
def main():

    # b. The code below initializes an empty list to store all policyholders.
    policyholders = []

    # Load existing policyholder data if available
    existing_policyholders = load_policyholder_data()
    for policyholder_data in existing_policyholders:
        policyholder = Policyholder(policyholder_data["policyholder_id"], policyholder_data["name"], policyholder_data["email"], policyholder_data["phone"])
        policyholder.status = policyholder_data["status"]
        policyholders.append(policyholder)

    # c. The code below provides a menu interface using a loop operation to allow the user to select the target task. The user can select from a range of options such as registering, suspending, updating, reactivating, displaying all policyholders, or searching for a policyholder. The user then responds with the corresponding letter via the input function "choice" which is converted to uppercase to prevent errors.
    while True:
        print("\n--- Policyholder Management Module ---")
        print("R - Register a new policyholder")
        print("P - Suspend a policyholder")
        print("U - Update policyholder details")
        print("A - Reactivate a policyholder")
        print("D - Display all policyholders")
        print("F - Find a policyholder")
        print("S - Save policyholder data")
        print("Q - Quit")
        choice = input("Enter your choice (R/P/U/A/D/F/S/Q): ").upper()

        # d. The code below implements one of the choices in 2c. It returns a message to register the policyholder if it doesn't exist in the policyholder management system.

        # d. i. This choice is for the registration of new policyholders.
        if choice == "R":
            register_policyholder(policyholders)

        # d. ii. This choice is for the suspension of existing policyholders.
        elif choice == "P":
            search_policyholder(policyholders)
            policyholder_id = input("Enter the Policyholder ID to suspend: ").strip()
            for policyholder in policyholders:
                if policyholder.policyholder_id == policyholder_id:
                    policyholder.suspend()
                    save_policyholder_data(policyholders)  # Save the updated policyholder list to JSON
                    break
            else:
                print("Policyholder not found.")

        # d. iii. This choice is for the update of existing policyholders' details.
        elif choice == "U":
            search_policyholder(policyholders)
            policyholder_id = input("Enter the Policyholder ID to update: ").strip()
            for policyholder in policyholders:
                if policyholder.policyholder_id == policyholder_id:
                    while True:
                        print("\nWhat would you like to update?")
                        print("1. Name")
                        print("2. Email")
                        print("3. Phone")
                        print("4. Exit Update Menu")
                        update_choice = input("Enter your choice (1/2/3/4): ")

                        if update_choice == "1":
                            new_name = input("Enter new name: ")
                            policyholder.update_name(new_name)
                        elif update_choice == "2":
                            new_email = input("Enter new email: ")
                            policyholder.update_email(new_email)
                        elif update_choice == "3":
                            new_phone = input("Enter new phone: ")
                            policyholder.update_phone(new_phone)
                        elif update_choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                        policyholder.display_details()
                    save_policyholder_data(policyholders)  # Save the updated policyholder list to JSON
                    break
            else:
                print("Policyholder not found.")

        # d. iv. This choice is for the reactivation of suspended policyholders.
        elif choice == "A":
            search_policyholder(policyholders)
            policyholder_id = input("Enter the Policyholder ID to reactivate: ").strip()
            for policyholder in policyholders:
                if policyholder.policyholder_id == policyholder_id:
                    policyholder.reactivate()
                    save_policyholder_data(policyholders)  # Save the updated policyholder list to JSON
                    break
            else:
                print("Policyholder not found.")

        # d. v. This choice is for displaying all policyholders.
        elif choice == "D":
            display_all_policyholders(policyholders)

        # d. vi. This choice is for searching for a policyholder by ID, name, email, or phone.
        elif choice == "F":
            search_policyholder(policyholders)

        # d. vii. This choice is for saving policyholder data to a JSON file.
        elif choice == "S":
            save_policyholder_data(policyholders)

        # d. viii. This choice is for quitting the policyholder management menu interface.
        elif choice == "Q":
            print("Exiting the program. Goodbye!")
            break

        # e. This else statement helps to handle input errors from users by returning an "invalid choice" prompt.
        else:
            print("Invalid choice. Please try again.")


# f. This code is used to run the entire program
if __name__ == "__main__":
    main()