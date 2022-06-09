from tkinter import DISABLED
from typing import List, Dict

from domain import NameStockError
from presenter.binds import bind_date_entry
from repository import StockRepository

import pandas as pd

from utils import date_range


class TabOneUseCase:
    def run(self, date_start, date_end, stock, get_info, var):

        get_info["state"] = DISABLED

        if len(stock.get()) < 4:
            raise NameStockError()

        stock_name_fixed = StockRepository().get_all_papers(stock)

        date_list = date_range(date_start.get_date(), date_end.get_date())
        list_info = StockRepository().get_json_and_build_fields(stock_name_fixed, date_list)

        self._create_dataframe_and_save(list_info, stock_name_fixed)

        bind_date_entry(date_start, date_end, get_info, stock, var)


    @staticmethod
    def _create_dataframe_and_save(list_info: List[Dict], stock_name_fixed: str):
        for info in list_info:
            df_daytrade_min = pd.DataFrame(
                {
                    "Date": info.get("date"),
                    "Open": info.get("open"),
                    "Close": info.get("close"),
                    "High": info.get("high"),
                    "Low": info.get("low"),
                    "Volume": info.get("volume"),
                }
            )

        df_daytrade_min.to_excel(f"{stock_name_fixed}.xlsx", index=False)
