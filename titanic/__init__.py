#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from views import View

if __name__ == '__main__':
    view = View()


    def print_menu():
        return '1. preprocess'

    while 1:
        menu = input(print_menu())
        if menu == '1':
            print(' ###preprocess### ')
            view.preprocess('train.csv', 'test.csv')
        else:
            break
