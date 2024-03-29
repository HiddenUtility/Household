
from pathlib import Path
from typing import override
from reader.rakuten.rakuten_card_file_reader import RakutenCardFileReader
from reader.rakuten.rakuten_card_file_path import RakutenCardFilePath
from reader.history_reader import HistoryReader
from config.data_direcotry_path import DataDirectoryPath
from config.card_names import CardNames
from reader.reading_datas import ReadingDatas

class RakutenReader(HistoryReader):
    DATA_PATH :Path = DataDirectoryPath.DATA_PAH
    __srcs : list[Path]
    def __init__(self) -> None:
        src = self.DATA_PATH / CardNames.RAKUTEN_CARD.name
        self.__srcs = [RakutenCardFilePath(f) for f in src.glob("*.csv") if f.is_file()]

    @override
    def load(self) -> list[ReadingDatas]:
        datas : list[ReadingDatas] = []
        for src in self.__srcs:
            datas += RakutenCardFileReader(src).run()
        return datas
            


