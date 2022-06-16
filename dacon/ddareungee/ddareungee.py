import pandas as pd
import sklearn
from icecream import ic
from sklearn.tree import DecisionTreeClassifier

from context.domains import *

'''
목표 : 해당 대회를 통해 각 날짜의 1시간 전의 기상상황을 활용 하여 따릉이 대여수를 예측해 보세요.
id              고유 id
hour            시간
temperature     기온
precipitation   비가 오지 않았으면 0, 비가 오면 1
windspeed       풍속(평균)
humidity        습도
visibility      시정(視程), 시계(視界)(특정 기상 상태에 따른 가시성을 의미)
ozone           오존
pm10            미세먼지(머리카락 굵기의 1/5에서 1/7 크기의 미세먼지)
pm2.5           미세먼지(머리카락 굵기의 1/20에서 1/30 크기의 미세먼지)
count           시간에 따른 따릉이 대여 수
'''


class Ddareungee(Reader):
    def __init__(self):
        self.file = File(context='./data/')

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. Preprocessing')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preproccess()
            else:
                break

    def preproccess(self):
        file = self.file
        file.fname = 'train'
        df = self.csv(file)
        ic(df.info())
        df.dropna(inplace=True)
        ic(df.info())


if __name__ == '__main__':
    Ddareungee().hook()
