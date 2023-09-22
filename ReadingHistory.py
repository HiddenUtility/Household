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
from datetime import date

from pathlib import Path
cd = Path.cwd()
sys.path.append(cd)

from MyUtil import myutil

import abc

####//Interface
class InterfaceReadingHistory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, other: object) -> None:
        raise NotImplementedError()
        

####//ParentClass
class ReadingHistory(InterfaceReadingHistory):
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
class JAcardReadingHistory(ReadingHistory):
    DATE_PATTERN = "%Y-%M-%D"
    COLNAME_DATE = "ご利用日"
    COLNAME_ITEM = "ご利用先／商品内容など"
    COLNAME_MONEY = "ご利用金額（円）"
    
    
    def __init__(self,dirpathSrc : Path):
        self.isErrorDirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
        self.listFilpath = [f for f in self.dirpathSrc.glob("*.csv") if f.is_file()]
        
    def _read_csv(self,f:Path):
        df = pd.read_csv(f, engine="python",encoding="cp932")
        df = df.dropna(subset=[self.COLNAME_DATE])
        
        
        return df
        
    def run():
        return
    
class UFJBankReadingHistory(ReadingHistory):
    def __init__(self,dirpathSrc : Path):
        self.isErrorDirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
    def run():
        return

class EposcardReadingHistory(ReadingHistory):
    def __init__(self,dirpathSrc : Path):
        self.isErrorDirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
    def run():
        return

class RakutencardReadingHistory(ReadingHistory):
    def __init__(self,dirpathSrc : Path):
        self.isErrorDirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
    def run():
        return


####データクラス
class ReadingDatas:
    datedata : date
    user : str
    imcome : int
    expenses : int
    itme : str
    dataname : str
    def __init__(self,
                 datedata : date,
                 user : str,
                 imcome : int,
                 expenses : int,
                 itme : str,
                 dataname : str
                 ):
        self.datedata : date
        self.user : str
        self.imcome : int
        self.expenses : int
        self.itme : str
        self.dataname : str
        
    def __eq__(self,other : ReadingDatas):
        if other is None or isinstance(other, ReadingDatas)==False:return False
        if self.datedata != other.datedata:return False
        if self.user != other.user:return False
        if self.imcome != other.imcome:return False
        if self.expenses != other.expenses:return False
        if self.itme != other.itme:return False
        if self.dataname != other.dataname:return False
        return True
        
    def __ne__(self):
        return self.__eq__()
        
    



if __name__ == '__main__':
    dirpathSrc = Path(r"C:\Users\nanik\OneDrive\物置\02_家計\01_家計簿")
    userNames = ["Hiroki","Haruna"]
    readingHistory = ReadingHistory(dirpathSrc,userNames)
    
    src = readingHistory.dirpathSrc.joinpath(userNames[1],readingHistory.JA_CARD)
    ja = JAcardReadingHistory(src)
    
    f = ja.listFilpath[0]
    
    df = ja._read_csv(f)
    

    
    
    
    