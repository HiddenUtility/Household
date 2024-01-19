
from src.ja_reader import JAReader
from src.rakuten_reader import RakutenReader
from src.ufj_reader import UFJReader
from src.epos_reader import EposReader
from src.reading_data import ReadingDatas

from pathlib import Path

from config.making_direcotry import MakingDirecotry

if __name__ == '__main__':
    
    MakingDirecotry().run()
