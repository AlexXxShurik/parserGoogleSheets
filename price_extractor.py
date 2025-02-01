import re

class PriceExtractor:
    @staticmethod
    def extract_price(text):
        """Извлекает последнюю найденную цену (от 4 до 7 цифр) в строке."""
        matches = re.findall(r'\b\d{4,7}\b', text)
        return int(matches[-1]) if matches else None