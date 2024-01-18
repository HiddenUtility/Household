
from __future__ import annotations
from typing import Final
from typing import override
from multiprocessing import Pool
from pathlib import Path
from src.reader import Reader      



class HistoryReader(Reader):
    JA_CARD : Final = "JA_CARD"
    UFJ_BANK : Final = "UFJ_BANK"
    EPOS_CARD : Final = "EPOS_CARD"
    RAKUTEN_CARD : Final = "RAKUTEN_CRAD"
    TOYOTA_CARD : Final = "TOYOTA_CARD"
    RAKUTEN_FAINANCE : Final = "RAKUTEN_FINANCE"
    RAKUTEN_BANK : Final = "RAKUTEN_BANK"
    LIST_DIRNAME = [JA_CARD,UFJ_BANK,EPOS_CARD,RAKUTEN_CARD,TOYOTA_CARD,RAKUTEN_FAINANCE,RAKUTEN_BANK]

    def __init__(self,src : Path,
                 user_names : list[str]
                 ):
        self.is_error_dirpath(src)
        self.is_error_list(user_names)
        self.__src = src
        self.__user_names = user_names
        self.__mkdir()
        
    def is_error_dirpath(self,src : Path):
        if src is None or isinstance(src, Path)==False :raise TypeError("dirpathSrc is NOT PathObject")
        if src.is_dir()==False:raise ValueError(f"{src} is mistaken")

    def is_error_list(self,user_names : list[str]):
        if user_names is None or isinstance(user_names, list)==False :raise TypeError("is NOT List")
        if len(user_names)==0:raise ValueError("list_ is Empty")

    def __mkdir(self):
        for user in self.__user_names:
            dirpathSrcUser = self.__src.joinpath(user)
            if dirpathSrcUser.is_dir()==False:dirpathSrcUser.mkdir()
            for dirname in self.LIST_DIRNAME:
                dirpathSrcData = dirpathSrcUser.joinpath(dirname)
                if dirpathSrcData.is_dir()==False:dirpathSrcData.mkdir()
    
    @override
    def run():
        return



    










    

    
    
    
    