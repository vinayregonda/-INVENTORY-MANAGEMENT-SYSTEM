from threading import Lock

class Database:
    def __init__(self):
        self.items = [
            {"id": 101, "name": "Laptop", "stock": 50, "cost_of_goods_sold": 5000, "historical_sales": 4500},
            {"id": 102, "name": "Silver", "stock": 30, "cost_of_goods_sold": 3000, "historical_sales": 2500},
            {"id": 103, "name": "Steel", "stock": 20, "cost_of_goods_sold": 2000, "historical_sales": 1800},
             {"id": 104, "name": "T-Shirts", "stock": 50, "cost_of_goods_sold": 3000, "historical_sales": 2000},
        ]
        self.locks = {item['id']: Lock() for item in self.items}

    def lock_item(self, item_id):
        return self.locks[item_id]

    def update_item(self, item_id, quantity):
        for item in self.items:
            if item['id'] == item_id:
                item['stock'] += quantity
                print(f"Updated {item['name']} stock to {item['stock']}")

    def add_item(self, item_id, name, stock, cost_of_goods_sold, historical_sales):
        new_item = {
            "id": item_id,
            "name": name,
            "stock": stock,
            "cost_of_goods_sold": cost_of_goods_sold,
            "historical_sales": historical_sales
        }
        self.items.append(new_item)
        self.locks[item_id] = Lock()

    def get_all_items(self):
        return self.items
