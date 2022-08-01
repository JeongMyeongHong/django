from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from urllib.parse import urljoin
import pandas as pd
from tqdm import tqdm
import folium
import googlemaps
import numpy as np


class Chicago:
    def __init__(self):
        self.url_base = 'http://www.chicagomag.com'
        self.url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'

    def process(self):
        soup = self.crawling()
        self.preprocessing(soup)
        self.marker()

    def crawling(self):
        # 시카고 매거진 크롤링
        url_base = self.url_base
        url_sub = self.url_sub
        url = url_base + url_sub
        html = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        soup = BeautifulSoup(html, "html.parser")
        print(len(soup.find_all('div', 'sammy')))  # 50
        # print(soup)
        return soup

    def preprocessing(self, soup):
        # 접근한 웹 페이지에서 원하는 데이터 추출하고 정리하기
        rank = []
        main_menu = []
        cafe_name = []
        url_add = []
        list_soup = soup.find_all('div', 'sammy')

        for item in list_soup:
            rank.append(item.find(class_='sammyRank').get_text())
            tmp_string = item.find(class_='sammyListing').get_text()
            main_menu.append(re.split(('\n|\r\n'), tmp_string)[0])
            cafe_name.append(re.split(('\n|\r\n'), tmp_string)[1])
            url_add.append(urljoin(self.url_base, item.find('a')['href']))

        print(rank[:5])  # ['1', '2', '3', '4', '5']
        print(main_menu[:5])  # ['BLT', 'Fried Bologna', 'Woodland Mushroom', 'Roast Beef', 'PB&L']
        print(cafe_name[:5])  # ['Old Oak Tap', 'Au Cheval', 'Xoco', 'Al’s Deli', 'Publican Quality Meats']
        print(url_add[:5])
        '''
        ['http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Old-Oak-Tap-BLT/',
         'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Au-Cheval-Fried-Bologna/',
         'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Xoco-Woodland-Mushroom/',
         'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Als-Deli-Roast-Beef/',
         'http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-in-Chicago-Publican-Quality-Meats-PB-L/']
        '''
        print(len(rank), len(main_menu), len(cafe_name), len(url_add))  # (50, 50, 50, 50)
        data = {'Rank': rank, 'Menu': main_menu, 'Cafe': cafe_name, 'URL': url_add}
        df = pd.DataFrame(data, columns=['Rank', 'Cafe', 'Menu', 'URL'])

        df.to_csv('./data/03. best_sandwiches_list_chicago.csv', sep=',',
                  encoding='UTF-8')
        df = pd.read_csv('./data/03. best_sandwiches_list_chicago.csv', index_col=0)
        print(df.head())

        price = []
        address = []
        for n in tqdm(df.index):
            html = urlopen(Request(df['URL'][n], headers={'User-Agent': 'Mozilla/5.0'}))
            soup_tmp = BeautifulSoup(html, 'lxml')
            gettings = soup_tmp.find('p', 'addy').get_text()
            price.append(gettings.split()[0][:-1])
            address.append(' '.join(gettings.split()[1:-2]))

        # print(price)  # 50개 가격 정보
        # print(address)  # 50개 주소
        print(df.head(10))
        print(len(price), len(address), len(df))

        df['Price'] = price
        df['Address'] = address
        df = df.loc[:, ['Rank', 'Cafe', 'Menu', 'Price', 'Address']]
        df.set_index('Rank', inplace=True)
        print(df.head())

        df.to_csv('./data/03. best_sandwiches_list_chicago2.csv', sep=',',
                  encoding='UTF-8')

    def marker(self):
        df = pd.read_csv('./data/03. best_sandwiches_list_chicago2.csv', index_col=0)
        print(df.head(5))

        gmaps_key = ""  # 2장에서 획득한 자신의 key를 사용합니다.
        gmaps = googlemaps.Client(key=gmaps_key)

        lat = []
        lng = []
        for n in tqdm(df.index):
            if df['Address'][n] != 'Multiple':
                target_name = df['Address'][n] + ', ' + 'Cicago'
                gmaps_output = gmaps.geocode(target_name)
                location_output = gmaps_output[0].get('geometry')
                lat.append(location_output['location']['lat'])
                lng.append(location_output['location']['lng'])
            else:
                lat.append(np.nan)
                lng.append(np.nan)

        df['lat'] = lat
        df['lng'] = lng
        mapping = folium.Map(location=[df['lat'].mean(), df['lng'].mean()],
                             zoom_start=11)
        for n in df.index:
            if df['Address'][n] != 'Multiple':
                folium.Marker([df['lat'][n], df['lng'][n]],
                              popup=df['Cafe'][n]).add_to(mapping)
        mapping.save('./save/map.html')


if __name__ == '__main__':
    Chicago().process()
