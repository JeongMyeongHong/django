#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplates
from titanic.views import TitanicView

if __name__ == '__main__':
    # view = TitanicView()
    def print_menu():
        return '1.템플릿 2.전처리'

    while 1:
        menu = input(print_menu())
        if menu == '1':
            print(' #### 1. 템플릿 #### ')
            titanicTemplates = TitanicTemplates(fname='train.csv')
            titanicTemplates.visualize()
            # view.preprocess('train.csv', 'test.csv')
        elif menu == '2':
            print(' #### 2. 전처리 #### ')
            titanicModel = TitanicModel(train_fname='train.csv', test_fname='test.csv')
        else:
            break
