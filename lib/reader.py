# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 05:45:55 2023

@author: iwill
"""
import abc
class Reader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, other: object) -> None:
        raise NotImplementedError()