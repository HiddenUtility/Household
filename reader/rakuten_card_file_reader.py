from reader.rakuten_card_file_path import RakutenCardFilePath
from reader.reading_data import ReadingDatas


class RakutenCardFileReader:
    def __init__(self, path: RakutenCardFilePath) -> None:
        if not isinstance(path, RakutenCardFilePath): raise TypeError()
        pass

    def run(self) -> ReadingDatas:
        return ReadingDatas()