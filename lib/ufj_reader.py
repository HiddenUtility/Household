# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 05:56:09 2023

@author: iwill
"""

from lib.history_reader import HistoryReader
from pathlib import Path
import pandas as pd

class UFJReader(HistoryReader):
    def __init__(self,dirpathSrc : Path):
        self.isErrorDirpath(dirpathSrc)
        self.dirpathSrc = dirpathSrc
    def run():
        return