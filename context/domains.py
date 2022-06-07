# dname, fname, train, test, id, label
from abc import *
from dataclasses import dataclass

import pandas


@dataclass()
class Dataset:
    dname: str
    sname: str
    fname: str
    train: pandas.core.frame.DataFrame
    test: pandas.core.frame.DataFrame
    id: str
    label: str

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self, value): self._dname = value

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, value): self._fname = value

    @property
    def train(self) -> pandas.core.frame.DataFrame: return self._train

    @train.setter
    def train(self, value): self._train = value

    @property
    def test(self) -> pandas.core.frame.DataFrame: return self._test

    @test.setter
    def test(self, value): self._test = value

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, value): self._id = value

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, value): self._label = value


# https://dojang.io/mod/page/view.php?id=2389
class PrinterBase(metaclass=ABCMeta):  # abc = abstract base class 의 약자
    @abstractmethod
    def dframe(self):
        pass


# new_file, csv, xls, json
class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass


# Printer extends Base
class Printer(PrinterBase):
    def __init__(self):
        pass

    def dframe(self):
        pass


# Reader extends Base
class Reader(ReaderBase):
    def __init__(self):
        pass

    def new_file(self):
        pass

    def csv(self):
        pass

    def xls(self):
        pass

    def json(self):
        pass