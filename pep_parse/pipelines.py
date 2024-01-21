import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    """Класс для обработки элементов, полученных при парсинге."""

    def open_spider(self, spider):
        """Метод для создания словаря"""
        self.results = defaultdict()

    def process_item(self, item, spider):
        """
        Метод обработки итемов, добавляет статус в словарь,
        если статус уже существует, прибавляет к значению +1.
        """
        if self.results.get(item['status']):
            self.results[item['status']] += 1
        else:
            self.results[item['status']] = 1
        return item

    def close_spider(self, spider):
        """Метод создает папку  и файл с подсчетом статусов."""
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows([
                ('Статус', 'Количество'),
                *self.results.items(),
                ('Всего', sum(self.results.values())),
            ])
