from reader.rakuten_card_file_columns import RakutenCardFileColumns
from reader.rakuten_card_file_path import RakutenCardFilePath
from reader.reading_datas import ReadingDatas
from pandas import DataFrame, read_csv
from datetime import datetime
from config import CardNames

class RakutenCardFileReader:
    __df : DataFrame
    def __init__(self, path: RakutenCardFilePath) -> None:
        if not isinstance(path, RakutenCardFilePath): raise TypeError()
        self.__df = read_csv(path.to_path(), 
                      encoding="utf-8", 
                      engine="python", 
                      usecols=[c.value for c in RakutenCardFileColumns],
                      )
    def __create_data(self, row: dict):
        return ReadingDatas(
            datetime_=datetime.strptime(row[RakutenCardFileColumns.DATE.value], r"%Y/%m/%d"),
            expenses=int(row[RakutenCardFileColumns.PAYMENT.value]),
            itme_name=row[RakutenCardFileColumns.SHOP_NAME.value],
            read_src_type=CardNames.RAKUTEN_CARD.name,
        )

    def run(self) -> list[ReadingDatas]:
        return [self.__create_data(row.to_dict()) for _,row in self.__df.iterrows()]