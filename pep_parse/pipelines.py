import os
import pathlib
from datetime import datetime


BASE_DIR = pathlib.Path('pipelines.py').parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses_count = {}
        current_time = datetime.now()
        str_time = current_time.strftime('%Y-%m-%d_%H-%M-%S')
        self.file = os.path.join(
            BASE_DIR, f'results/status_summary_{str_time}.csv'
        )

    def process_item(self, item, spider):
        status = item['status']
        if status in self.statuses_count:
            self.statuses_count[status] += 1
        else:
            self.statuses_count[status] = 1
        with open(self.file, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.statuses_count.items():
                f.write(f'{status},{count}\n')
            total = sum(self.statuses_count.values())
            f.write(f'Total,{total}\n')
        return item

    def close_spider(self, spider):
        pass
