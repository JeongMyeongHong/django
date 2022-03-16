from context.domains import Dataset
from context.models import Model
from icecream import ic
import matplotlib.pyplot as plt

'''
데이터 시각화
엔티티(개체)를 차트로 표현하는 것

'Survived', 'Pclass', 'Sex', 'Embarked'4개만 그린다.
템플릿 메소드 패턴으로 구현하라.
'''


class TitanicTemplates:
    dataset = Dataset()
    model = Model()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)

    def visualize(self) -> None:
        this = self.entity
        ic(f'트레인의 타입 : {type(this)}')
        ic(f'트레인의 컬럼 : {this.columns}')
        ic(f'트레인의 상위 5행 : {this.head()}')
        ic(f'트레인의 하위 5행 : {this.tail()}')
        f, ax = plt.subplots(2, 2, figsize=(18, 8))
        self.draw_survived(this, ax)
        self.draw_pclass(this, ax)
        self.draw_sex(this, ax)
        # self.draw_embarked(this, ax)
        plt.show()

    @staticmethod
    def draw_survived(this, ax) -> None:
        entity = 'Survived'
        ax1 = ax[0][0]
        ax1.set_title(entity)
        ax1.plot(this[entity])

    @staticmethod
    def draw_pclass(this, ax) -> None:
        entity = 'Pclass'
        ax2 = ax[0][1]
        ax2.set_title(entity)
        ax2.plot(this[entity])

    @staticmethod
    def draw_sex(this, ax) -> None:
        entity = 'Sex'
        ax3 = ax[1][0]
        ax3.set_title(entity)
        ax3.plot(this[entity])

    # @staticmethod
    # def draw_embarked(this, ax) -> None:
    #     ax[1][1].plot(this['Embarked'])

