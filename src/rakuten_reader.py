

from src.history_reader import HistoryReader
from pathlib import Path
import pandas as pd

class RakutenReader(HistoryReader):
    def __init__(self,dirpathSrc : Path):
        self.is_error_dirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
    def run():
        return
