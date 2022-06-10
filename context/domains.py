# dname, fname, train, test, id, label
from abc import *
from dataclasses import dataclass

import googlemaps
import pandas as pd


@dataclass
class Dataset:
    dname: str
    sname: str
    fname: str
    train: pd.core.frame.DataFrame
    test: pd.core.frame.DataFrame
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
    def train(self) -> pd.core.frame.DataFrame: return self._train

    @train.setter
    def train(self, value): self._train = value

    @property
    def test(self) -> pd.core.frame.DataFrame: return self._test

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


@dataclass
class File(object):
    context: str
    fname: str
    dframe: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe


# https://dojang.io/mod/page/view.php?id=2389
# new_file, csv, xls, json
class ReaderBase(metaclass=ABCMeta):  # abc = abstract base class 의 약자

    @staticmethod
    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self, fname):
        pass

    @abstractmethod
    def xls(self, fname, header, cols, skiprow):
        pass

    @abstractmethod
    def json(self, fname):
        pass


# Reader extends Base
class Reader(ReaderBase):

    @staticmethod
    def new_file(file) -> str:
        return file.context + file.fname

    def csv(self, file):
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    # header, column 두개 옵션 걸어 주기.
    def xls(self, file, header, cols, skiprow):
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=cols, skiprows=[skiprow])

    def json(self, file):
        return pd.read_json(f'{self.new_file(file)}.json')

    @staticmethod
    def gmaps() -> googlemaps.client.Client:
        return googlemaps.Client(key='')
        # 키는 무조건 지우고 커밋하자.

    @staticmethod
    def dframe(this):
        print('*' * 100)
        print(f'1. Target type \n {type(this)} ')
        print(f'2. Target column \n {this.columns} ')
        print(f'3. Target top 1개 행\n {this.head(1)} ')
        print(f'4. Target bottom 1개 행\n {this.tail(1)} ')
        print(f'4. Target null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)
