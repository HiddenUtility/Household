from reader.history_reader import HistoryReader
from pathlib import Path
import pandas as pd

class UFJReader(HistoryReader):
    def __init__(self,dirpathSrc : Path):
        self.is_error_dirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
    def load():
        return