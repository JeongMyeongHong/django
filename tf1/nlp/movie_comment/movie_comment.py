from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
from collections import defaultdict

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False
import numpy as np
from context.domains import *
import math


class MovieComment(Reader):
    def __init__(self, k=0.5):
        self.file = File(context='./save/')
        self.k = k  # naive_bayes 설정값
        self.word_probs = []  # naive_bayes 설정값

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. Preprocessing: text mining(Crwaling)')
            print('2. Preprocessing: Tokenize')
            print('3. Preprocessing: Embedding')
            print('4. 다음 영화 댓글이 긍정인지 부정인지 ratio 값으로 판단하시오\n'
                  '너무 좋아요. 내 인생의 최고의 명장 영화\n'
                  '이렇게 졸린 영화는 처음이야\n')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.crawling()
            elif menu == '2':
                # self.tokenization()
                pass
            elif menu == '3':
                self.preproccess()
            elif menu == '4':
                print(self.naive_bayes_classifier('너무 좋아요. 내 인생의 최고의 명장 영화'))
                print(self.naive_bayes_classifier('계속 졸았어요 돈이 너무 아깝네요'))
                print(self.naive_bayes_classifier('시리즈 내용이 다 비슷하네요'))
                print(self.naive_bayes_classifier('이렇게 졸린거 다신 안봐요'))
                print(self.naive_bayes_classifier('정말 재미 없어요 다섯번 졸았네요'))
                print(self.naive_bayes_classifier('보다가 그냥 나왔어요'))
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
        return pd.read_csv(self.new_file(file), delimiter='\t',
                           names=['title', 'score', 'comment', 'label'])

    def preproccess(self):
        df = self.stereotype()
        df = self.drop_garvage(df)
        # self.analyze_reviews(df)
        self.visualize_reviews(df)

        return df

    @staticmethod
    def drop_garvage(df):
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

    @staticmethod
    def analyze_reviews(df):
        movie_lst = df.title.unique()
        print('전체 영화 편수 =', len(movie_lst))
        print(movie_lst[:10])
        cnt_movie_reviews = df.title.value_counts()
        print(cnt_movie_reviews[:20])
        # info_movie = df.groupby('title')['score'].describe()
        # info_movie.sort_values(by=['count'], axis=0, ascending=False)
        # ic(info_movie)
        # 아래 람다로 대체
        ic((lambda a, b: df.groupby(a)[b].describe())('title', 'score').sort_values(by=['count'], axis=0,
                                                                                    ascending=False))

    @staticmethod
    def visualize_reviews(df):
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
        MovieComment.rating_distribution(top10, avg_score)

    @staticmethod
    def rating_distribution(top_10, avg_score):
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()

        for title, avg, ax in zip(avg_score.keys(), avg_score.values(), axs):
            num_reviews = len(top_10[top_10['title'] == title])
            x = np.arange(num_reviews)
            y = top_10[top_10['title'] == title]['score']
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
            num_reviews = len(top_10[top_10['title'] == title])
            values = top_10[top_10['title'] == title]['label'].value_counts()
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.pie(values,
                   autopct='%1.1f%%',
                   colors=colors,
                   shadow=True,
                   startangle=90)
            ax.axis('equal')
        plt.show()

    def naive_bayes_classifier(self, doc):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        training_set = self.load_corpus(path)
        word_probs = self.train(training_set)
        point = self.classify(word_probs, doc)
        return self.postprocess(point)

    @staticmethod
    def load_corpus(path):
        corpus = pd.read_table(path, names=['title', 'point', 'doc', 'label'], encoding='UTF-8')
        corpus.drop(labels=['title', 'label'], axis=1, inplace=True)
        corpus.dropna(inplace=True)
        corpus.drop_duplicates(inplace=True)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, training_set):
        counts = defaultdict(lambda: [0, 0])
        for point, doc in training_set:
            # 영화리뷰가 text 일때만 카운드
            if self.isNumber(doc) is False:
                # 리뷰를 띄어쓰기 단위로 토크나이징
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 7 else 1] += 1
        return counts

    @staticmethod
    def isNumber(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def word_probabilities(self, counts, total_class0, total_class1, k):
        """pass"""
        # 단어의 빈도수를 [단어, p(w|긍정), p(w|부정)] 형태로 변환
        return [(w, (class0 + k) / (total_class0 + 2 * k), (class1 + k) / (total_class1 + 2 * k)) for
                w, (class0, class1) in counts.items()]

    def train(self, training_set):
        print('-------------- 훈련 시작 --------')
        # 범주0 (긍정) 과 범주1(부정) 문서의 수를 세어줌
        num_class0 = len([1 for point, _ in training_set if point > 7])
        num_class1 = len(training_set) - num_class0
        # train
        word_counts = self.count_words(training_set)
        return self.word_probabilities(word_counts, num_class0, num_class1, self.k)

    def classify(self, word_probs, doc):
        return self.class0_probability(word_probs, doc)

    @staticmethod
    def class0_probability(word_probs, doc):
        # 별도 토크나이즈 하지 않고 띄어쓰기만
        print(f'코멘트 : {doc}', end='\t\t\t')
        docwords = doc.split()
        # 초기값은 모두 0으로 처리
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        # 모든 단어에 대해 반복
        for word, prob_if_class0, prob_if_class1 in word_probs:
            # 만약 리뷰에 word 가 나타나면 해당 단어가 나올 log 에 확률을 더 해줌
            if word in docwords:
                log_prob_if_class0 += math.log(prob_if_class0)
                log_prob_if_class1 += math.log(prob_if_class1)
            # 만약 리뷰에 word 가 나타나지 않는다면
            # 해당 단어가 나오지 않을 log 에 확률을 더해줌
            # 나오지 않을 확률은 log(1 - 나올 확률) 로 계산
            else:
                log_prob_if_class0 += math.log(1.0 - prob_if_class0)
                log_prob_if_class1 += math.log(1.0 - prob_if_class1)
        prob_if_class0 = math.exp(log_prob_if_class0)
        prob_if_class1 = math.exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    @staticmethod
    def postprocess(point):
        if point > 0.8:
            return f'토마토 싱싱하네요. 평점 : {round(point * 10, 2)}'
        elif point > 0.5:
            return f'토마토 맛없어요. 평점 : {round(point*10, 2)}'
        else:
            return f'토마토 썩었습니다. 평점 : {round(point*10, 2)}'


if __name__ == '__main__':
    MovieComment().hook()
