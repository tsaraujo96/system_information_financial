from tkinter import DISABLED

from pandas import ExcelWriter

from domain import NameStockError
from presenter.binds import bind_date_entry
from repository import StockRepository, OptionRepository

import pandas as pd

from utils import date_range


class TabOneUseCase:
    def run(self, date_start, date_end, stock, get_info, var):

        get_info["state"] = DISABLED

        if len(stock.get()) < 4:
            raise NameStockError()

        stock_name_fixed = StockRepository().get_all_papers(stock)

        date_list = date_range(date_start.get_date(), date_end.get_date())
        stock_data_frame = StockRepository().get_json_and_build_fields(stock_name_fixed, date_list)

        correct_name = self._fix_name_stock(stock_name_fixed)
        option_data_frame = OptionRepository().get_all_opcoes(correct_name)

        self._saves_in_excel(stock_data_frame, option_data_frame, correct_name)

        bind_date_entry(date_start, date_end, get_info, stock, var)

    @staticmethod
    def _fix_name_stock(stock_name_fixed: str) -> str:
        try:
            correct_name = stock_name_fixed.split(".")[0]
        except IndexError:
            correct_name = stock_name_fixed

        return correct_name

    @staticmethod
    def _saves_in_excel(stock_data_frame: pd.DataFrame, option_data_frame: pd.DataFrame, correct_name: str):

        list_dataframe = [(stock_data_frame, 'Ações'), (option_data_frame, 'Opções')]

        with ExcelWriter(f"{correct_name}.xlsx") as writer:
            for df in list_dataframe:
                df[0].to_excel(writer, df[1], index=False)
