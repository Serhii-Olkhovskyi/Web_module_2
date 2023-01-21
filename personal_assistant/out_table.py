from tabulate import tabulate
from abc import ABC, abstractmethod


class AbstractOutInfo(ABC):
    @abstractmethod
    def out_all_info(self):
        pass


class OutInfo(AbstractOutInfo):
    table_format = 'pipe'
    table_showindex = 'always'

    def __init__(self, data, header_table):
        self.data = data
        self.headers = header_table

    def out_all_info(self):
        print(tabulate(self.data, headers=self.headers, tablefmt=self.table_format, showindex=self.table_showindex))
