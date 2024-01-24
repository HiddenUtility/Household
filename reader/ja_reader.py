from reader.history_reader import HistoryReader
from pathlib import Path
import pandas as pd

class JAReader(HistoryReader):
    DATE_PATTERN = "%Y-%M-%D"
    COLNAME_DATE = "ご利用日"
    COLNAME_ITEM = "ご利用先／商品内容など"
    COLNAME_MONEY = "ご利用金額（円）"
    
    
    def __init__(self,dirpathSrc : Path):
        self.is_error_dirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
        self.listFilpath = [f for f in self.dirpathSrc.glob("*.csv") if f.is_file()]
        
    def _read_csv(self,f:Path):
        df = pd.read_csv(f, engine="python",encoding="cp932")
        df = df.dropna(subset=[self.COLNAME_DATE])
        
        
        return df
        
    def load():
        return