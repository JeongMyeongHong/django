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

    def preprocess(self):
        print('전처리')
        self.create_train()
        self.sibSp_garbage()
        self.parch_garbage()
        self.ticket_garbage()
        self.cabin_garbage()
        self.create_label()

        self.embarked_nominal()
        self.name_nominal()
        self.pclass_ordinal()
        self.fare_ratio()
        self.sex_ordinal()
        self.age_ratio()

    def create_label(self) -> object:
        pass

    def create_train(self) -> object:
        pass

    def drop_feature(self) -> object:
        pass

    def pclass_ordinal(self) -> object:
        pass

    def name_nominal(self) -> object:
        pass

    def sex_ordinal(self) -> object:
        pass

    def age_ratio(self) -> object:
        pass

    def sibSp_garbage(self) -> object:
        pass

    def parch_garbage(self) -> object:
        pass

    def ticket_garbage(self) -> object:
        pass

    def fare_ratio(self) -> object:
        pass

    def cabin_garbage(self) -> object:
        pass

    def embarked_nominal(self) -> object:
        pass
