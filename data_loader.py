import pandas as pd

class DataLoader:
    def __init__(self, shop_file, price_file):
        self.shop_file = shop_file
        self.price_file = price_file

    def load_shop_data(self):
        """Загружает данные о товарах из Excel."""
        return pd.read_excel(self.shop_file)

    def load_price_data(self):
        """Загружает данные о ценах и поставщиках из Excel."""
        return pd.read_excel(self.price_file)
