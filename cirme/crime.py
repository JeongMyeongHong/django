from pprint import pprint

import numpy as np
import pandas as pd

from context.domains import *
import folium
from sklearn import preprocessing


# 표준화 -> 스케일링 -> 리스케일링(정규화)


class Solution(Reader):
    def __init__(self, context):
        self.context = context
        self.file = File(context=self.context)
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. crime_in_seoul.csv, 구글맵 API 를 이용해서 서울시내 경찰서 주소목록파일(police_pos.csv)을 작성하시오.')
            print('2. us-states.json, us_unemployment.csv 를 이용해서 미국 실업률 지도를 작성하시오.')
            print('3. cctv_in_seoul.csv, pop_in_seoul.csv 를 이용해서 서울시내 경찰서 주소목록파일(cctv_pop.csv)을 작성하시오.')
            print('4. save_police_norm')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.save_police_pos(self)
            if menu == '2':
                self.folium_test_us(self)
            if menu == '3':
                self.save_cctv_pos(self)
            if menu == '4':
                self.save_police_norm()
            elif menu == '0':
                break

    #  crime_in_seoul
    @staticmethod
    def save_police_pos(s):
        s.file.fname = 'crime_in_seoul'
        crime = s.csv(s.file)
        station_names = []
        [station_names.append(f'서울{name[:-1]}경찰서') for name in crime['관서명']]
        # print(f'station_names range : {len(station_names)}') # 서울 시내 경찰서 31개
        gmaps = s.gmaps()
        # [print(f'name {i} = {name}') for i, name in enumerate(station_names)]
        a = gmaps.geocode('서울관악경찰서', language='ko')
        # 서울종암경찰서의 주소가 21.12.20에 이전해서 Null로 떨어짐
        # 현재 주소 : 서울특별시 성북구 화랑로7길 32
        # 주소를 수동으로 일단 넣어줌.
        # print(a)

        station_addrs = []
        station_lats = []
        station_lngs = []

        for i, name in enumerate(station_names):  # 서울 시내 경찰서 리스트 확인
            temp = gmaps.geocode(name, language='ko')
            if name == '서울종암경찰서':
                temp = [{'address_components':
                             [{'long_name': '32', 'short_name': '32', 'types': ['premise']},
                              {'long_name': '화랑로7길', 'short_name': '화랑로7길',
                               'types': ['political', 'sublocality', 'sublocality_level_4']},
                              {'long_name': '성북구', 'short_name': '성북구',
                               'types': ['political', 'sublocality', 'sublocality_level_1']},
                              {'long_name': '서울특별시', 'short_name': '서울특별시',
                               'types': ['administrative_area_level_1', 'political']},
                              {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
                              {'long_name': '03130', 'short_name': '03130', 'types': ['postal_code']}],
                         'formatted_address': '대한민국 서울특별시 성북구 화랑로7길 32',
                         'geometry':
                             {'location': {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                              'location_type': 'ROOFTOP',
                              'viewport':
                                  {'northeast':
                                       {'lat': 37.57331688029149,
                                        'lng': 127.0003063802915},
                                   'southwest':
                                       {'lat': 37.57061891970849,
                                        'lng': 126.9976084197085}}},
                         'partial_match': True, 'place_id': 'ChIJc0PIxSCjfDURWuMVOPZrMTM',
                         'plus_code': {'compound_code': 'HXCX+QH 대한민국 서울특별시', 'global_code': '8Q98HXCX+QH'},
                         'types': ['establishment', 'point_of_interest', 'police']}]

            # print(f'name {i} = {temp[0].get("formatted_address")}')
            station_addrs.append(temp[0].get("formatted_address"))
            t_loc = temp[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])

        # gu_names = []
        #
        # for name in station_addrs:
        #     temp = name.split()
        #     gu_name = [gu for gu in temp if gu[-1] == '구'][0]
        #     gu_names.append(gu_name)
        # 이 코드를 전부 comprehension 으로 바꾸면 아래 처럼 된다.

        # [[gu_names.append(gu) for gu in name.split() if gu[-1] == '구'] for name in station_addrs]

        crime['구별'] = [[gu for gu in name.split() if gu[-1] == '구'][0] for name in station_addrs]
        print(crime['구별'])
        [print(gu) for gu in crime['구별']]
        crime.to_csv('./save/police_pos.csv', index=False)

    #  cctv_in_seoul
    @staticmethod
    def save_cctv_pos(s):
        file_cctv = File(context=s.context, fname='cctv_in_seoul')
        file_pop = File(context=s.context, fname='pop_in_seoul')
        cctv = s.csv(file_cctv)
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        cctv.drop(columns=[cctv.columns[i] for i in range(2, 6)], axis=1, inplace=True)
        # cctv.append({'구별': '합계', '소계': 30}, ignore_index=True)
        print(cctv)

        pop = s.xls(file=file_pop, header=1, cols='B, D, G, J, N', skip_row=2)
        pop_rename_columns = ['구별', '인구수', '한국인', '외국인', '고령자']
        pop.rename(columns=
                   {pop_column: column for pop_column, column in zip(pop.columns, pop_rename_columns)}, inplace=True)
        pop.dropna(how='all', inplace=True)
        col_names = ['외국인', '고령자']
        for col_name in col_names:
            pop[f'{col_name}비율'] = pop[col_name] / pop['인구수'] * 100
        print(pop)

        cctv_pop = cctv.merge(pop)
        print(cctv_pop)

        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """

        # cctv_pop.to_csv('./save/cctv_pop.csv')

    # 정규화 normalization = rescaling
    def save_police_norm(self):
        file = self.file
        file.context = './save/'
        file.fname = 'police_pos'
        police_pos = self.csv(file)
        police = pd.pivot_table(police_pos, index='구별', aggfunc=np.sum)
        for crime_rate_column, crime_column in zip(self.crime_rate_columns, self.crime_columns):
            police[crime_rate_column] = police[f'{crime_column} 검거'] / police[f'{crime_column} 발생'] * 100
            police.drop(columns={f'{crime_column} 검거'}, inplace=True)
            police.rename(columns={f'{crime_column} 발생': f'{crime_column}'}, inplace=True)

        # for i in self.crime_rate_columns:
        #     police[i].loc[police[i] > 100] = 100  # 데이터값이 기간 오류로 100을 넘으면 100으로 계산

        for column in self.crime_rate_columns:
            [for (i, e) in enumerate(police[column]) if e > 100]


        # def f(x):
        #     if x > 100: x = 100
        #
        # for i in self.crime_rate_columns:
        #     police[i].apply(f, axis=1)
        print(police)
        # police.to_csv('./save/police.csv')
        """          
        피쳐 스케일링(Feature scalining)은 해당 피쳐들의 값을 일정한 수준으로 맞춰주는 것이다.
        이때 적용되는 스케일링 방법이 표준화(standardization) 와 정규화(normalization)다.
        
        1단계: 표준화(공통 척도)를 진행한다.
            표준화는 정규분포를 데이터의 평균을 0, 분산이 1인 표준정규분포로 만드는 것이다.
            x = (x - mu) / sigma
            scale = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
        2단계: 이상치 발견 및 제거
        3단계: 정규화(공통 간격)를 진행한다.
            정규화에는 평균 정규화, 최소-최대 정규화, 분위수 정규화가 있다.
             * 최소최대 정규화는 모든 데이터를 최대값을 1, 최솟값을 0으로 만드는 것이다.
            도메인은 데이터의 범위이다.
            스케일은 데이터의 분포이다.
            목적은 도메인을 일치시키거나 스케일을 유사하게 만든다.    
        """
        x = police[self.crime_rate_columns].values
        min_max_scalar = preprocessing.MinMaxScaler()
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        # police_norm.to_csv('./save/police_norm.csv', sep=',', encoding='UTF-8')

    def folium_test(self):
        pass
        # m = folium.Map(location=[37.60388169879458, 127.04001571848704])
        # m.save("./save/folium_test.html")

    # geo_simple
    @staticmethod
    def draw_crime_map(s):
        s.file.fname = 'geo_simple'
        s.dframe(s.json(s.file))

    def save_csv(self, fname):
        self.file.fname = fname
        # print(self.csv(self.file))
        return self.csv(self.file)

    @staticmethod
    def save_json(s, fname):
        s.file.fname = fname
        # print(self.json(self.file))
        return s.json(s.file)

    @staticmethod
    def folium_test_us(s):
        unemployment = s.save_csv('us_unemployment')
        states = './data/us-states.json'
        bins = list(unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))

        m = folium.Map(location=[48, -102], zoom_start=4)  # 미국 지도

        folium.Choropleth(
            geo_data=states,  # 지도 데이터
            name="choropleth",
            data=unemployment,  # 지도 위에 얹을 데이터
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Unemployment Rate (%)",
            bins=bins,  # scale
            reset=True  # 값이 바뀌면 계속 바뀌도록 함.
        ).add_to(m)
        print("저장 주석 걸었음.")
        # m.save("./save/folium_test.html")


if __name__ == '__main__':
    solution = Solution(context='./data/')
    solution.hook()
