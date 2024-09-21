from alert_system import AlertSystem

class TransferSystem:
    def __init__(self, inventory):
        self.inventory = inventory
        self.alert_system = AlertSystem()
    
    def manage_transfer(self):
        item_id = int(input("Enter Item ID to transfer: "))
        source = input("Enter source warehouse: ")
        target = input("Enter target warehouse: ")
        quantity = int(input("Enter quantity to transfer: "))
        delay = int(input("Enter transfer delay in hours: "))
        
        if delay > 3:
            print(f"Delay in shipment for Item {item_id}. Delay: {delay} hours.")
            self.alert_system.send_shipment_delay_alert(item_id, delay)
        else:
            with self.inventory.db.lock_item(item_id):
                self.transfer_item(item_id, source, target, quantity)
    
    def transfer_item(self, item_id, source, target, quantity):
        print(f"Transferring {quantity} units of Item {item_id} from {source} to {target}.")
        # Here, you'd include the actual transfer logic
        print(f"Transferred {quantity} units of Item {item_id} from {source} to {target}.")
