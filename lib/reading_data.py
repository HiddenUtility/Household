# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 05:48:05 2023

@author: iwill
"""
from __future__ import annotations
from datetime import date

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
        
    def __ne__(self,other : ReadingDatas):
        return not self.__eq__(other) 
        
    
