import re

class PatternBuilder:
    @staticmethod
    def build_pattern(keywords):
        """Создаёт регулярное выражение на основе списка ключевых слов."""
        return re.compile(
            rf".*{re.escape(keywords[1])} .*{re.escape(keywords[2])}.{re.escape(keywords[6])}.*"
            rf"({re.escape(keywords[4])}|{re.escape(keywords[3])}).*",
            re.IGNORECASE
        )