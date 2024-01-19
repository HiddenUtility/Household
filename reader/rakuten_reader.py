
from pathlib import Path
from typing import override
from reader.history_reader import HistoryReader
from config.data_direcotry_path import DataDirectoryPath
from config.card_names import CardNames

class RakutenReader(HistoryReader):
    DATA_PATH :Path = DataDirectoryPath.DATA_PAH
    __srcs : list[Path]
    def __init__(self) -> None:
        src = self.DATA_PATH / CardNames.RAKUTEN_CARD.name
        self.__srcs = [f for f in src.glob("*.csv") if f.is_file()]


    @override
    def run(self):
        pass
