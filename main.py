import pandas as pd
from data_loader import DataLoader
from product_parser import ProductParser
from pattern_builder import PatternBuilder
from price_extractor import PriceExtractor
from utils import Utils

def main():
    # Пути к файлам
    shop_file = "./data/products.xlsx"
    price_file = "./data/price.xlsx"
    result_file = "./data/result.xlsx"

    # Загружаем данные
    data_loader = DataLoader(shop_file, price_file)
    shop_df = data_loader.load_shop_data()
    price_df = data_loader.load_price_data()

    # Создаём словарь товаров
    parsed_products = shop_df.apply(lambda row: ProductParser(row).parse(), axis=1).tolist()
    result_products = {}

    # Создаём словарь цен и поставщиков
    price_dict = Utils.create_price_supplier_dict(price_df)

    # Применяем фильтрацию через регулярные выражения
    for item in parsed_products:
        product_name = item[0]
        pattern = PatternBuilder.build_pattern(item)
        filtered_entries = {
            price: supplier for price, supplier in price_dict.items() if pattern.search(price.lower())
        }

        # Записываем найденные цены и поставщиков
        price_supplier_list = []
        for price_text, supplier in filtered_entries.items():
            price_actual = PriceExtractor.extract_price(price_text)
            if price_actual:
                price_supplier_list.extend([price_actual, supplier])

        if price_supplier_list:
            result_products[product_name] = price_supplier_list

    # Преобразуем результат в DataFrame
    columns = Utils.create_columns(result_products)

    result_df = pd.DataFrame([
        [product] + values + [''] * (len(columns) - len(values) - 1)
        for product, values in result_products.items()
    ], columns=columns)

    # Сохраняем результат
    result_df.to_excel(result_file, index=False)
    print(f"Файл {result_file} успешно сохранён.")

if __name__ == "__main__":
    main()
