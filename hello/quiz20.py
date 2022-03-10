from pprint import pprint
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd


def extract_info(soup, tag, info) -> []:
    return [i.get_text().strip() for i in soup.find_all(tag, {"class": info})]


def make_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return BeautifulSoup(urlopen(req), 'lxml')


def dict1(keys, values) -> {}:
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict


def dict2(keys, values) -> {}:
    dict = {}
    for i, key in enumerate(keys):
        dict[key] = values[i]
    return dict


def dict3(keys, values) -> {}:
    dict = {}
    for key, value in zip(keys, values):
        dict[key] = value
    return dict


class Quiz20:
    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))  # [1, 2, 3, 4]list           [1, 2, 3, 4] <class 'list'>
        print(list1[0], list1[-1], list1[-2], list1[1:3])  # 1, 4, 3, [2, 3, 4]         1 4 3 [2, 3]
        list2 = ['math', 'english']
        print(list2[0])  # math                       math
        print(list2[0][1])  # a                          a
        list3 = [1, '2', [1, 2, 3]]
        print(list3)  # [1, 2, [1, 2, 3]]          [1, '2', [1, 2, 3]]
        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)  # [1, 2, 3, 4, 5]            [1, 2, 3, 4, 5]
        print(2 * list4)  # [1, 2, 3, 1, 2, 3]         [1, 2, 3, 1, 2, 3]
        list4.append(list5)
        print(list4)  # [1, 2, 3, 4, 5]            [1, 2, 3, [4, 5]]
        list4[-2:] = []
        print(list4)  # [1, 2, 3]                  [1, 2]
        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)  # [[1, 2], [0, 5]]           [[1, 2], [0, 5]]
        print(c[0][1])  # 2                          2
        c[0][1] = 10
        print(c)  # [[1, 10], [0, 5]]          [[1, 10], [0, 5]]
        a = range(10)
        print(a)  # range(10)                  range(0, 10)
        print(sum(a))  # 45                         45
        b = [2, 10, 0, -2]
        print(sorted(b))  # [-2, 0, 2, 10]             [-2, 0, 2, 10]
        b.index(0)
        len(b)
        print(b.index(0), len(b))  # 2, 4                       2 4
        return None

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))  # (1, 2) <class: tuple>     (1, 2) <class 'tuple'>
        # a[0] = 4                                                # Error: tuple can't update
        # 'tuple' object does not support item assignment
        a = (1, 2)
        b = (0, (1, 4))
        print(a + b)  # (1, 2, 0, (1, 4))         (1, 2, 0, (1, 4))
        return None

    def quiz22dict(self) -> str:
        a = {'class': ['deep learning', 'machine learning'], 'num_students': [40, 20]}
        print(a)
        # {'class': ['deep learning', 'machine learning'], 'num_students': [40, 20]}
        # {'class': ['deep learning', 'machine learning'], 'num_students': [40, 20]}

        print(type(a))  # <class: dict>             <class 'dict'>
        print(a['class'])  # ['deep learning', 'machine learning']     ['deep learning', 'machine learning']

        a['grade'] = ['A', 'B', 'C']
        print(a.keys())  # class num_students grade          dict_keys(['class', 'num_students', 'grade'])

        print(list(a.keys()))  # [class, num_students, grade]      ['class', 'num_students', 'grade']

        print(a.values())  # 'deep learning' 'machine learning' ['A', 'B', 'C']
        # dict_values([['deep learning', 'machine learning'], [40, 20], ['A', 'B', 'C']])

        print(a.items())  # I don't know
        # dict_items([('class', ['deep learning', 'machine learning']), ('num_students', [40, 20]), ('grade', ['A', 'B', 'C'])])

        print(a.get('class'))  # ['deep learning', 'machine learning']
        # ['deep learning', 'machine learning']

        print('class' in a)  # I don't know              True
        return None

    def quiz23listcom(self) -> str:
        print('-' * 10 + 'legacy' + '-' * 10)
        a = []
        for i in range(5):
            a.append(i)
        print(a)

        print('-' * 10 + 'comprehension' + '-' * 10)
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        n = 100
        soup = make_soup('https://music.bugs.co.kr/chart/track/realtime/total')
        # infos = [extract_info(soup, 'p', i)[0:n] for i in ['artist', 'title']]
        # print(infos)
        #[print(f'{i}등', (j, k)) for i, (j, k) in enumerate(zip(infos[0], infos[1]), start=1)]
        artists = extract_info(soup, 'p', 'artist')[:n]
        titles = extract_info(soup, 'p', 'title')[:n]
        return dict3(titles, artists)

    def quiz25dictcom(self) -> str:
        return None

    def quiz26map(self) -> str:
        return None

    def quiz27melon(self) -> str:
        soup = make_soup('https://www.melon.com/chart/index.htm?dayTime=2022030816')
        a = extract_info(soup, 'div', 'ellipsis rank01')
        print(a)
        return None

    def quiz28dataframe(self) -> None:
        #dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')


    def quiz29(self) -> str:
        return None
