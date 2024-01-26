from __future__ import annotations
from datetime import datetime


class ReadingDatas:
    __datetime : datetime
    __filename : str
    __imcome : int
    __expenses : int
    __itme_name : str
    __read_src_type : str

    def __init__(self,
                 datetime_ : datetime = datetime(2000,1,1),
                 filename : str = "nodata",
                 itme_name : str = "nodata",
                 read_src_type : str = "nodata",
                 imcome : int = 0,
                 expenses : int = 0,
                 ):
        self.__datetime = datetime_
        self.__filename = filename
        self.__imcome = imcome
        self.__expenses = expenses
        self.__itme_name = itme_name
        self.__read_src_type = read_src_type

        
    def __eq__(self,other : ReadingDatas):
        if other is None or isinstance(other, ReadingDatas)==False:return False
        if self.__datetime != other.datetime:return False
        if self.__filename != other.user:return False
        if self.__imcome != other.imcome:return False
        if self.__expenses != other.expenses:return False
        if self.__itme_name != other.itme:return False
        if self.__read_src_type != other.name:return False
        return True
        
    def __ne__(self,other : ReadingDatas):
        return not self.__eq__(other)
    
    def __str__(self) -> str:
        return f"""
"date" : "{self.__datetime}"
"filename" : "{self.__filename}"
"imcom" : "{self.__imcome}"
"expenses" : "{self.__expenses}"
"item" : "{self.__itme_name}"
"name" : "{self.__read_src_type}"
"""


    @property
    def datetime(self) -> datetime:
        return self.__datetime
    
    @property
    def user(self) -> str:
        return self.__filename

    @property
    def imcome(self) -> datetime:
        return self.__imcome
    
    @property
    def expenses(self) -> str:
        return self.__expenses
    
    @property
    def itme(self) -> datetime:
        return self.__itme_name
    
    @property
    def name(self) -> str:
        return self.__read_src_type