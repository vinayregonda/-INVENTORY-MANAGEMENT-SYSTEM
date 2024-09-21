from utils.database import Database

class Inventory:
    def __init__(self):
        self.db = Database()

    def update_inventory(self):
        item_id = int(input("Enter Item ID to update: "))
        quantity = int(input("Enter quantity to add: "))
        
        with self.db.lock_item(item_id):
            self.db.update_item(item_id, quantity)
            print(f"Updated Item {item_id} by {quantity} units.")

    def add_material(self):
        item_id = int(input("Enter new Item ID: "))
        name = input("Enter new Item name: ")
        stock = int(input("Enter initial stock quantity: "))
        cost_of_goods_sold = float(input("Enter cost of goods sold: "))
        historical_sales = float(input("Enter historical sales: "))
        
        self.db.add_item(item_id, name, stock, cost_of_goods_sold, historical_sales)
        print(f"Added new material: ID {item_id}, Name {name}, Stock {stock}.")

    def display_stock_levels(self):
        items = self.db.get_all_items()
        print("\n--- Current Stock Levels ---")
        for item in items:
            print(f"ID: {item['id']}, Name: {item['name']}, Stock: {item['stock']}")
