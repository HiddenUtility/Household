# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:47:25 2023

@author: uh
"""

from __future__ import annotations
from typing import Final
from typing import Optional

import sys
import pandas as pd, numpy as np
from multiprocessing import Pool
import multiprocessing


from pathlib import Path
cd = Path.cwd()
sys.path.append(cd)



from lib.reader import Reader

        

####//ParentClass
class HistoryReader(Reader):
    JA_CARD : Final = "JA_CARD"
    UFJ_BANK : Final = "UFJ_BANK"
    EPOS_CARD : Final = "EPOS_CARD"
    RAKUTEN_CARD : Final = "RAKUTEN_CRAD"
    TOYOTA_CARD : Final = "TOYOTA_CARD"
    RAKUTEN_FAINANCE : Final = "RAKUTEN_FINANCE"
    RAKUTEN_BANK : Final = "RAKUTEN_BANK"
    LIST_DIRNAME = [JA_CARD,UFJ_BANK,EPOS_CARD,RAKUTEN_CARD,TOYOTA_CARD,RAKUTEN_FAINANCE,RAKUTEN_BANK]
    def __init__(self,dirpathSrc : Path,
                 userNames : list[str]
                 ):
        self.isErrorDirpath(dirpathSrc)
        self.isErrorList(userNames)
        self.dirpathSrc = dirpathSrc
        self.userNames = userNames
        #ディレクトリ構造を決定する。
        self.__mkdir()
        
    def isErrorDirpath(self,dirpathSrc : Path):
        if dirpathSrc is None or isinstance(dirpathSrc, Path)==False :raise TypeError("dirpathSrc is NOT PathObject")
        if dirpathSrc.is_dir()==False:raise ValueError(f"{dirpathSrc} is mistaken")
    def isErrorList(self,list_ : list[str]):
        if list_ is None or isinstance(list_, list)==False :raise TypeError("is NOT List")
        if len(list_)==0:raise ValueError("list_ is Empty")
    def __mkdir(self):
        for user in self.userNames:
            dirpathSrcUser = self.dirpathSrc.joinpath(user)
            if dirpathSrcUser.is_dir()==False:dirpathSrcUser.mkdir()
            for dirname in self.LIST_DIRNAME:
                dirpathSrcData = dirpathSrcUser.joinpath(dirname)
                if dirpathSrcData.is_dir()==False:dirpathSrcData.mkdir()
    
    
    def run():
        return

####//PackageClass

    










    

    
    
    
    