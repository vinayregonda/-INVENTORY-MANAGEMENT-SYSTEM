import pandas as pd

class Forecasting:
    def __init__(self, inventory):
        self.inventory = inventory

    def generate_reports(self):
        print("Generating reports...")

        self.calculate_inventory_turnover()
        self.generate_forecast_report()

    def calculate_inventory_turnover(self):
        print("Calculating inventory turnover...")
        data = pd.DataFrame(self.inventory.db.get_all_items())
        data["turnover_rate"] = data["cost_of_goods_sold"] / data["stock"]

        print("\n--- Inventory Turnover Report ---")
        print(data[["id", "name", "turnover_rate"]])

    def generate_forecast_report(self):
        print("Generating forecast report...")
        data = pd.DataFrame(self.inventory.db.get_all_items())
        data["forecasted_sales"] = data["historical_sales"] * 1.1  # 10% growth

        print("\n--- Forecast Report ---")
        print(data[["id", "name", "forecasted_sales"]])
