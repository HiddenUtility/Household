from pathlib import Path
from typing import override
from reader.epos.EposCardFilePath import EposCardFilePath
from reader.epos.EposCardFileReader import EposCardFileReader
from reader.history_reader import HistoryReader
from config.data_direcotry_path import DataDirectoryPath
from config.card_names import CardNames
from reader.reading_datas import ReadingDatas
from reader.reading_datas import ReadingDatas
from config import CardNames

class EposReader(HistoryReader):
    DATA_PATH :Path = DataDirectoryPath.DATA_PAH
    __srcs : list[Path]
    def __init__(self) -> None:
        src = self.DATA_PATH / CardNames.EPOS_CARD.name
        self.__srcs = [EposCardFilePath(f) for f in src.glob("*.csv") if f.is_file()]

    @override
    def load(self) -> list[ReadingDatas]:
        datas : list[ReadingDatas] = []
        for src in self.__srcs:
            datas += EposCardFileReader(src).run()
        return datas
            

