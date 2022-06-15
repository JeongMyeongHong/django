from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgunsl.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
import numpy as np
from context.domains import *
import math
import re


class MovieComment(Reader):
    def __init__(self):
        self.file = File(context='./save/')
        self.movie_comments = pd.DataFrame()

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. Preprocessing')
            print('11. Crwaling')
            print('2. Tokenize')
            print('3. Embedding')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preproccess()
            elif menu == '11':
                self.crawling()
            elif menu == '2':
                self.tokenization()
            elif menu == '3':
                self.preproccess()
            else:
                break

    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        f = open(self.new_file(file), 'w', encoding='UTF-8')

        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                rev_lst = []
                title = rev.select_one('a.movie').text.strip()
                score = rev.select_one('div.list_netizen_score > em').text.strip()
                comment = rev.select_one('br').next_sibling.strip()

                # -- 긍정/부정 리뷰 레이블 설정
                if int(score) >= 8:
                    label = 1  # -- 긍정 리뷰 (8~10점)
                elif int(score) <= 4:
                    label = 0  # -- 부정 리뷰 (0~4점)
                else:
                    label = 2

                f.write(f'{title}\t{score}\t{comment}\t{label}\n')
        f.close()

    def stereotype(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        self.movie_comments = pd.read_csv(self.new_file(file), delimiter='\t',
                           names=['title', 'score', 'comment', 'label'])

    def preproccess(self):
        self.stereotype()
        df = self.drop_garvage()
        return df

    def drop_garvage(self):
        df = self.movie_comments
        # ic(df.info())
        ''' RangeIndex: 5000 entries, 0 to 4999
            Data columns (total 4 columns):
             #   Column   Non-Null Count  Dtype 
            ---  ------   --------------  ----- 
             0   title    5000 non-null   object
             1   score    5000 non-null   int64 
             2   comment  4683 non-null   object
             3   label    5000 non-null   int64 
             comment에 null값이 있고, 중복되는 부분도 있기 때문에 이를 제거해준다.
        '''
        df_reviews = df.dropna()
        df_reviews = df_reviews.drop_duplicates(['comment'])
        return df_reviews

    def analyze_reviews(self):
        df = self.movie_comments
        movie_lst = df.title.unique()
        cnt_movie_reviews = df.title.value_counts()
        info_movie = df.groupby('title')['score'].describe()
        info_movie.sort_values(by=['count'], axis=0, ascending=False)
        # ic(info_movie)

    def visualize_reviews(self):
        df = self.movie_comments
        top10 = df.title.value_counts().sort_values(ascending=False)[:10]
        top10_title = top10.index.tolist()
        top10_reviews = df[df['title'].isin(top10_title)]

        print(top10_title)
        print(top10_reviews.info())
        movie_title = top10_reviews.title.unique().tolist()  # -- 영화 제목 추출
        avg_score = {}  # -- {제목 : 평균} 저장
        for t in movie_title:
            avg = top10_reviews[top10_reviews['title'] == t]['score'].mean()
            avg_score[t] = avg

        plt.figure(figsize=(10, 5))
        plt.title('영화 평균 평점 (top 10: 리뷰 수)\n', fontsize=17)
        plt.xlabel('영화 제목')
        plt.ylabel('평균 평점')
        plt.xticks(rotation=20)

        for x, y in avg_score.items():
            color = np.array_str(np.where(y == max(avg_score.values()), 'orange', 'lightgrey'))
            plt.bar(x, y, color=color)
            plt.text(x, y, '%.2f' % y,
                     horizontalalignment='center',
                     verticalalignment='bottom')
        plt.show()

        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()

        for title, avg, ax in zip(avg_score.keys(), avg_score.values(), axs):
            num_reviews = len(top10_reviews[top10_reviews['title'] == title])
            x = np.arange(num_reviews)
            y = top10_reviews[top10_reviews['title'] == title]['score']
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.set_ylim(0, 10.5, 2)
            ax.plot(x, y, 'o')
            ax.axhline(avg, color='red', linestyle='--')  # -- 평균 점선 나타내기

        plt.show()

        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()
        colors = ['pink', 'gold', 'whitesmoke']
        labels = ['1 (8~10점)', '0 (1~4점)', '2 (5~7점)']

        for title, ax in zip(avg_score.keys(), axs):
            num_reviews = len(top10_reviews[top10_reviews['title'] == title])
            values = top10_reviews[top10_reviews['title'] == title]['label'].value_counts()
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.pie(values,
                   autopct='%1.1f%%',
                   colors=colors,
                   shadow=True,
                   startangle=90)
            ax.axis('equal')
        plt.show()

    def analyze_keyword(self):
        df_reviews = self.preproccess()
        pos_reviews = df_reviews[df_reviews['label'] == 1]
        neg_reviews = df_reviews[df_reviews['label'] == 0]

    def tokenization(self):
        pass

if __name__ == '__main__':
    MovieComment().hook()
