from inventory import Inventory
from reorder import ReorderSystem
from transfer import TransferSystem
from forecasting import Forecasting
from alert_system import AlertSystem
from security import Security
from utils.config import USERS

def main():
    inventory = Inventory()
    reorder_system = ReorderSystem(inventory)
    transfer_system = TransferSystem(inventory)
    forecasting = Forecasting(inventory)
    alert_system = AlertSystem()
    
    print("Welcome to the Inventory Management System")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = Security().authenticate(username, password, USERS)
    if not user:
        print("Authentication failed. Exiting system.")
        return

    role = user['role']
    print(f"Welcome {username}! Your role is {role}.")
    
    while True:
        print("\n--- Menu ---")
        print("1. Update Inventory (Admin Only)")
        print("2. Add New Material (Admin Only)")
        print("3. Check Reorder (Admin Only)")
        print("4. Manage Transfers (Admin Only)")
        print("5. Generate Reports (All Roles)")
        print("6. Display Stock Levels (All Roles)")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1' and role == 'Admin':
            inventory.update_inventory()
        
        elif choice == '2' and role == 'Admin':
            inventory.add_material()
        
        elif choice == '3' and role == 'Admin':
            reorder_system.check_reorder()
        
        elif choice == '4' and role == 'Admin':
            transfer_system.manage_transfer()
        
        elif choice == '5':
            forecasting.generate_reports()
        
        elif choice == '6':
            inventory.display_stock_levels()
        
        elif choice == '7':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice or insufficient permissions.")

if __name__ == "__main__":
    main()
