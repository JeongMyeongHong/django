from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train.drop('Survived', axis=1, inplace=True)
        this = self.drop_feature(this, 'Cabin', 'Parch', 'Ticket', 'SibSp')
        self.print_this(this)
        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)'''
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')
        ic(f'2. Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4. Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 : {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 : {type(this.id)}\n')
        ic(f'10. id 의 상위 10개 : {this.id[:10]}\n')
        print('*' * 100)

    @staticmethod
    def create_train(this) -> object:
        return this

    @staticmethod
    def drop_feature(this, *feature):
        # [[j.drop(i, axis=1, inplace=True) for i in feature] for j in [this.train, this.test]]
        [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]
        return this

    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this
