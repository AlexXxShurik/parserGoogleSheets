import pandas as pd

class Utils:
    @staticmethod
    def create_price_supplier_dict(price_df):
        """Создаёт словарь {прайс: поставщик} из price_df."""
        return {
            str(row['прайс']).strip(): str(row['поставщик']).strip()
            for _, row in price_df.iterrows()
            if pd.notna(row.get('прайс')) and pd.notna(row.get('поставщик'))
        }

    @staticmethod
    def create_columns(result_products):
        """Создаёт список столбцов для DataFrame."""
        max_columns = max(len(values) for values in result_products.values()) if result_products else 0
        columns = ['Наше название'] + [f'цена {i//2 + 1}' if i % 2 == 0 else f'поставщик {i//2 + 1}' for i in range(max_columns)]
        return columns