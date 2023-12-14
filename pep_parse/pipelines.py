import os
import pathlib
from collections import defaultdict
from datetime import datetime


BASE_DIR = pathlib.Path('pipelines.py').parent
STR_TIME = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
RESULTS_DIR = f'results/status_summary_{STR_TIME}.csv'


class PepParsePipeline:

    def __init__(self):
        self.statuses_count = defaultdict(int)

    def open_spider(self, spider):
        self.file = os.path.join(BASE_DIR, RESULTS_DIR)

    def process_item(self, item, spider):
        status = item['status']
        self.statuses_count[status] += 1
        with open(self.file, mode='w', encoding='utf-8') as f:
            summary = ['Статус,Количество\n']
            for status, count in self.statuses_count.items():
                summary.append(f'{status},{count}\n')
            total = sum(self.statuses_count.values())
            summary.append(f'Total,{total}\n')
            f.writelines(summary)
        return item

    def close_spider(self, spider):
        pass
