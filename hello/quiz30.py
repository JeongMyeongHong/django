import string
import pandas as pd
from icecream import ic
from hello.domains import my_random


class Quiz30:
    def quiz30_df_4_by_3(self) -> object:
        ls = [[j * 3 + i for i in range(1, 4)] for j in range(4)]
        df = pd.DataFrame(ls, index=range(1, 5), columns=['A', 'B', 'C'])
        ic(df)
        return df

    def quiz31_rand_2_by_3(self) -> object:
        ls = [[my_random(10, 100) for i in range(3)] for j in range(2)]
        df = pd.DataFrame(ls)
        ic(df)
        return df

    def quiz32_df_grade(self) -> object:
        subjects = ['국어', '영어', '수학', '사회']
        names = [''.join([string.ascii_letters[my_random(0, 51)] for i in range(5)]) for i in range(10)]
        ls = {names[j]: [my_random(0, 100) for i in range(4)] for j in range(10)}
        df = pd.DataFrame.from_dict(ls, orient='index', columns=subjects)
        print(df)

        return None

    def quiz33(self) -> object:
        column_name = ['나이', '성별', '잔고', '결혼여부']
        df_list = [[20, '남자', 2000, '미혼'],
                   [50, '여자', 15000, '결혼'],
                   [48, '남자', 20000, '결혼'],
                   [32, '여자', 800, '미혼'],
                   [28, '남자', 1200, '결혼'],
                   [38, '여자', 3600, '결혼']]
        df = pd.DataFrame(df_list, columns=column_name)
        print(df.tail())
        return df

    def quiz34(self) -> str:
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
