import re
import pandas as pd

class ProductParser:
    # Словарь перевода цветов внутри класса
    color_translation = {
        'серебро': 'silver', 'серый космос': 'gray cosmos', 'голубой': 'light blue',
        'желтый': 'yellow', 'розовое золото': 'rose gold', 'розовый': 'pink',
        'фиолетовый': 'purple', 'серый': 'graphite', 'белый': 'white',
        'синий': 'blue', 'золотой': 'desert', 'черный': 'black',
        'зеленый': 'green', 'серебристый': 'silvery', 'темно-синий': 'dark blue',
        'коралловый': 'coral', 'сиреневый': 'lavender', 'бежевый': 'beige',
        'красный': 'red', 'оранжевый': 'orange', 'коричневый': 'brown',
        'золото': 'desert', 'зелёный': 'green'
    }

    def __init__(self, row):
        self.row = row

    def parse(self):
        """Обрабатывает строку и возвращает список характеристик."""
        name = str(self.row.get('Наименование', '')).strip()
        model = str(self.row.get('Модель', '')).strip().lower()
        manufacturer = str(self.row.get('Производитель', '')).strip().lower()

        if model and manufacturer:
            model = model.replace(manufacturer, "").strip()
            model = re.sub(r'\b(?:galaxy|nubia)\b', '', model).strip()
            if model.isdigit():
                model = f"{manufacturer} {model}"

        ram = str(int(self.row['Оперативная память (Gb)'])) if pd.notna(self.row.get('Оперативная память (Gb)')) else '-'
        color = str(self.row.get('Цвет', '')).strip().lower()
        translated_color = self.color_translation.get(color, '')
        storage = str(self.row.get('Встроенная память', '')).strip()
        extracted_storage = re.search(r'\d+', storage)
        extracted_storage = extracted_storage.group() if extracted_storage else ''

        return [name, model, ram, color, translated_color, storage, extracted_storage]
