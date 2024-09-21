class ReorderSystem:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def check_reorder(self):
        items = self.inventory.db.get_all_items()
        reorder_needed = False
        print("Checking for reorder requirements...")
        
        for item in items:
            if item['stock'] < 30:  # Threshold for reorder
                self.reorder_item(item['id'])
                reorder_needed = True
        
        if not reorder_needed:
            print("No items need reordering.")
    
    def reorder_item(self, item_id):
        print(f"Reordering Item {item_id}.")
        # This is a placeholder. In a real scenario, more complex logic would be applied.
        print(f"Item {item_id} has been reordered.")
