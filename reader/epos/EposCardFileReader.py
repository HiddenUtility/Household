from datetime import datetime
from pandas import DataFrame, read_csv
from config import CardNames
from config.card_names import CardNames
from reader.epos.EposCardFileColumns import EposCardFileColumns
from reader.epos.EposCardFilePath import EposCardFilePath
from reader.reading_datas import ReadingDatas


class EposCardFileReader:
    __df : DataFrame
    def __init__(self, path: EposCardFilePath) -> None:
        if not isinstance(path, EposCardFilePath): raise TypeError()
        self.__filename = path.name
        self.__df = read_csv(path.to_path(),
                      encoding="cp932",
                      engine="python",
                      usecols=[c.value for c in EposCardFileColumns],
                      skiprows=1,
                      ).fillna("")
    def __create_data(self, row: dict) -> ReadingDatas:
        return ReadingDatas(
            datetime_=datetime.strptime(row[EposCardFileColumns.DATE.value], r"%Y年%m月%d日"),
            filename=self.__filename,
            expenses=int(row[EposCardFileColumns.PAYMENT.value]),
            itme_name=row[EposCardFileColumns.SHOP_NAME.value],
            read_src_type=CardNames.EPOS_CARD.name,
        )


    def run(self) -> list[ReadingDatas]:
        ret: list[ReadingDatas] = []
        for _,row in self.__df.iterrows():
            if row[EposCardFileColumns.SHOP_NAME.value] == "":
                break
            try:
                ret.append(self.__create_data(row.to_dict()))
            except Exception:
                print(row.to_dict())
                break
        return ret