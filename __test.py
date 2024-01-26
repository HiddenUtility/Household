
from reader.ja_reader import JAReader
from reader.rakuten.rakuten_reader import RakutenReader
from reader.ufj_reader import UFJReader
from reader.epos.epos_reader import EposReader
from reader.reading_datas import ReadingDatas

from pathlib import Path

from src.making_direcotry import MakingDirecotry

if __name__ == '__main__':
    
    MakingDirecotry().run()

    datas : list[ReadingDatas] = []
    # datas = RakutenReader().load()
    [print(d) for d in datas]

    datas = EposReader().load()
    [print(d) for d in datas]