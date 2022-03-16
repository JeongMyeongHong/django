import pandas
import pandas as pd
from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel:
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.dataset.train = self.model.new_model(train_fname)
        self.dataset.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.dataset.train.columns}')
        ic(f'트레인 헤드 {self.dataset.train.head()}')
        ic(self.dataset.train)

    def preprocess(self) -> object:
        print('전처리')
        df = self.create_train()
        df = self.drop_feature(df)
        df = self.create_label(df)

        df = self.embarked_nominal(df)
        df = self.name_nominal(df)
        df = self.pclass_ordinal(df)
        df = self.fare_ratio(df)
        df = self.sex_ordinal(df)
        df = self.age_ratio(df)
        return df

    def create_train(self) -> object:
        return self.dataset.train

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def drop_feature(df) -> object:
        for i in ['SibSp', 'Parch', 'Ticket', 'Cabin']:
            df = df.drop(columns=[i])
        return df

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def sex_ordinal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def fare_ratio(df) -> object:
        return df

    @staticmethod
    def embarked_nominal(df) -> object:
        return df
