from context.domains import *
import folium


class Solution(Reader):
    def __init__(self, context):
        self.context = context
        self.file = File(context=self.context)
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']

    #  crime_in_seoul
    def save_police_pos(self):
        self.file.fname = 'crime_in_seoul'
        crime = self.csv(self.file)
        station_names = []
        [station_names.append(f'서울{name[:-1]}경찰서') for name in crime['관서명']]
        # print(f'station_names range : {len(station_names)}') # 서울 시내 경찰서 31개
        gmaps = self.gmaps()
        [print(f'name {i} = {name}') for i, name in enumerate(station_names)]
        a = gmaps.geocode('서울관악경찰서', language='ko')
        # 서울종암경찰서의 주소가 21.12.20에 이전해서 Null로 떨어짐
        # 현재 주소 : 서울특별시 성북구 화랑로7길 32
        # 주소를 수동으로 일단 넣어줌.
        print(a)

        for i, name in enumerate(station_names):  # 서울 시내 경찰서 리스트 확인
            temp = gmaps.geocode(name, language='ko')
            if name == '서울종암경찰서':
                temp = [{'address_components':
            [{'long_name': '32', 'short_name': '32', 'types': ['premise']},
             {'long_name': '화랑로7길', 'short_name': '화랑로7길', 'types': ['political', 'sublocality', 'sublocality_level_4']},
             {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']},
             {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']},
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

            print(f'name {i} = {temp[0].get("formatted_address")}')

        station_addrs = []
        station_lats = []
        station_lngs = []

    #  cctv_in_seoul
    def save_cctv_pos(self):
        file_cctv = File(context=self.context, fname='cctv_in_seoul')
        file_pop = File(context=self.context, fname='pop_in_seoul')
        cctv = self.csv(file_cctv)
        pop = self.xls(file=file_pop, header=1, cols='B, D, G, J, N', skiprow=2)
        # self.dframe(pop)
        print(pop.head(10))

    # 구글 맵으로 가져 올꺼라 없음.
    def save_police_norm(self):
        pass

    def folium_test(self):
        pass
        # m = folium.Map(location=[37.60388169879458, 127.04001571848704])
        # m.save("./save/folium_test.html")

    # geo_simple
    def draw_crime_map(self):
        self.file.fname = 'geo_simple'
        self.dframe(self.json(self.file))

    def save_csv(self, fname):
        self.file.fname = fname
        # print(self.csv(self.file))
        return self.csv(self.file)

    def save_json(self, fname):
        self.file.fname = fname
        # print(self.json(self.file))
        return self.json(self.file)

    def folium_test_us(self):
        unemployment = self.save_csv('us_unemployment')
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
        m.save("./save/folium_test.html")



if __name__ == '__main__':
    solution = Solution(context='./data/')
    solution.folium_test_us()
