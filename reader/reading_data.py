from __future__ import annotations
from datetime import datetime

class ReadingDatas:
    __datetime : datetime
    __user : str
    __imcome : int
    __expenses : int
    __itme : str
    __name : str

    def __init__(self,
                 datetime_ : datetime,
                 user : str,
                 imcome : int,
                 expenses : int,
                 itme : str,
                 name : str
                 ):
        self.__datetime = datetime_
        self.__user = user
        self.__imcome = imcome
        self.__expenses = expenses
        self.__itme = itme
        self.__name = name

        
    def __eq__(self,other : ReadingDatas):
        if other is None or isinstance(other, ReadingDatas)==False:return False
        if self.__datetime != other.datetime:return False
        if self.__user != other.user:return False
        if self.__imcome != other.imcome:return False
        if self.__expenses != other.expenses:return False
        if self.__itme != other.itme:return False
        if self.__name != other.name:return False
        return True
        
    def __ne__(self,other : ReadingDatas):
        return not self.__eq__(other)
    

    @property
    def datetime(self) -> datetime:
        return self.__datetime
    
    @property
    def user(self) -> str:
        return self.__user

    @property
    def imcome(self) -> datetime:
        return self.__imcome
    
    @property
    def expenses(self) -> str:
        return self.__expenses
    
    @property
    def itme(self) -> datetime:
        return self.__itme
    
    @property
    def name(self) -> str:
        return self.__name