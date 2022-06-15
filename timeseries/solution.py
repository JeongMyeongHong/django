# https://github.com/PinkWink/DataScience/blob/master/source_code/07.%20Time%20Series%20Data%20Handle.ipynb

import warnings
import numpy as np
from fbprophet import Prophet

from context.domains import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from icecream import ic
from pandas_datareader import data
# import fix_yahoo_finance as yf
# 위에꺼 안됩니다.(19.10.30) 기준 설치가 되지 않음.
# pip install yfinance 이걸로 라이브러리 설치 후 임포트트
import yfinance as yf

warnings.filterwarnings("ignore")
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False


class Solution(Reader):
    def __init__(self):
        self.future = None
        self.file = File(context='./data/')

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1.Numpy의 polyfit으로 회귀(regression) 분석')
            print('2.Prophet 모듈을 이용한 forecast 예측')
            print('3.Seasonal 시계열 분석으로 주식 데이터 분석')
            print('4.Growth Model과 Holiday Forecast')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.analyze_by_polyfit()
            elif menu == '2':
                self.forecast_by_prophet()
            elif menu == '3':
                self.analyze_data_of_stock()
            elif menu == '4':
                self.forecast_holliday()
            else:
                break

    @staticmethod
    def error(f, x, y):
        return np.sqrt(np.mean((f(x) - y) ** 2))

    def read_PinkWinkWebTraffic(self):
        file = self.file
        file.fname = '08. PinkWink Web Traffic.csv'
        pinkwink_web = pd.read_csv(self.new_file(file),
                                   encoding='utf-8', thousands=',', names=['date', 'hit'], index_col=0)
        return pinkwink_web[pinkwink_web['hit'].notnull()]

    def analyze_by_polyfit(self):
        pinkwink_web = self.read_PinkWinkWebTraffic()
        # print(pinkwink_web)
        pinkwink_web['hit'].plot(figsize=(12, 4), grid=True)
        time = np.arange(0, len(pinkwink_web))
        traffic = pinkwink_web['hit'].values
        fx = np.linspace(0, time[-1], 1000)

        fp1 = np.polyfit(time, traffic, 1)
        f1 = np.poly1d(fp1)

        f2p = np.polyfit(time, traffic, 2)
        f2 = np.poly1d(f2p)

        f3p = np.polyfit(time, traffic, 3)
        f3 = np.poly1d(f3p)

        f15p = np.polyfit(time, traffic, 15)
        f15 = np.poly1d(f15p)

        # print(Solution.error(f1, time, traffic))
        # print(Solution.error(f2, time, traffic))
        # print(Solution.error(f3, time, traffic))
        # print(Solution.error(f15, time, traffic))

        plt.figure(figsize=(10, 6))
        plt.scatter(time, traffic, s=10)

        plt.plot(fx, f1(fx), lw=4, label='f1')
        plt.plot(fx, f2(fx), lw=4, label='f2')
        plt.plot(fx, f3(fx), lw=4, label='f3')
        plt.plot(fx, f15(fx), lw=4, label='f15')

        plt.grid(True, linestyle='-', color='0.75')

        plt.legend(loc=2)
        # plt.show()

    def forecast_by_prophet(self):
        pinkwink_web = self.read_PinkWinkWebTraffic()
        df = pd.DataFrame({'ds': pinkwink_web.index, 'y': pinkwink_web['hit']})
        df.reset_index(inplace=True)
        df['ds'] = pd.to_datetime(df['ds'], format="%y. %m. %d.")
        del df['date']
        m = Prophet(yearly_seasonality=True, daily_seasonality=True)
        m.fit(df)
        self.future = m.make_future_dataframe(periods=60)
        future = self.future
        # ic(future.tail())
        forecast = m.predict(future)
        colunms = ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
        # ic(forecast[colunms].tail())
        m.plot(forecast)
        m.plot_components(forecast)
        # plt.show()
        return m

    def analyze_data_of_stock(self):
        yf.pdr_override()
        m = self.forecast_by_prophet()
        future = self.future

        start_date = '1990-1-1'
        end_date = '2017-6-30'
        KIA = data.get_data_yahoo('000270.KS', start_date, end_date)
        # ic(KIA.head())
        KIA['Close'].plot(figsize=(12, 6), grid=True)
        plt.show()

        forecast = m.predict(future)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
        KIA_trunc = KIA[:'2016-12-31']
        # print(KIA_trunc)

        df = pd.DataFrame({'ds': KIA_trunc.index, 'y': KIA_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']
        # ic(df.head())
        m = Prophet(daily_seasonality=True)
        m.fit(df)
        future = m.make_future_dataframe(periods=365)
        # ic(future.tail())
        forecast = m.predict(future)
        # ic(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
        m.plot(forecast)
        m.plot_components(forecast)

        start_date = '2014-1-1'
        end_date = '2017-7-31'
        KIA = data.get_data_yahoo('000270.KS', start_date, end_date)
        KIA['Close'].plot(figsize=(12, 6), grid=True)

        KIA_trunc = KIA[:'2017-05-31']
        KIA_trunc['Close'].plot(figsize=(12, 6), grid=True)

        df = pd.DataFrame({'ds': KIA_trunc.index, 'y': KIA_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']

        m = Prophet(daily_seasonality=True)
        m.fit(df)

        future = m.make_future_dataframe(periods=61)
        ic(future.tail())

        forecast = m.predict(future)
        m.plot(forecast)

        plt.figure(figsize=(12, 6))
        plt.plot(KIA.index, KIA['Close'], label='real')
        plt.plot(forecast['ds'], forecast['yhat'], label='forecast')
        plt.grid()
        plt.legend()
        plt.show()

    def forecast_holliday(self):
        file = self.file
        file.fname = '08. example_wp_R.csv'
        df = pd.read_csv(self.new_file(file))
        df['y'] = np.log(df['y'])
        df['cap'] = 8.5
        m = Prophet(growth='logistic', daily_seasonality=True)
        ic(m.fit(df))
        future = m.make_future_dataframe(periods=1826)
        future['cap'] = 8.5
        fcst = m.predict(future)
        m.plot(fcst)
        # plt.show()

        forecast = m.predict(future)
        m.plot_components(forecast)
        # plt.show()

        file.fname = '08. example_wp_peyton_manning.csv'
        df = pd.read_csv(self.new_file(file))
        df['y'] = np.log(df['y'])
        m = Prophet(daily_seasonality=True)
        m.fit(df)
        future = m.make_future_dataframe(periods=366)
        df.y.plot(figsize=(12, 6), grid=True)
        plt.show()

        playoffs = pd.DataFrame({
            'holiday': 'playoff',
            'ds': pd.to_datetime(['2008-01-13', '2009-01-03', '2010-01-16',
                                  '2010-01-24', '2010-02-07', '2011-01-08',
                                  '2013-01-12', '2014-01-12', '2014-01-19',
                                  '2014-02-02', '2015-01-11', '2016-01-17',
                                  '2016-01-24', '2016-02-07']),
            'lower_window': 0,
            'upper_window': 1,
        })
        superbowls = pd.DataFrame({
            'holiday': 'superbowl',
            'ds': pd.to_datetime(['2010-02-07', '2014-02-02', '2016-02-07']),
            'lower_window': 0,
            'upper_window': 1,
        })
        holidays = pd.concat((playoffs, superbowls))
        m = Prophet(holidays=holidays, daily_seasonality=True)
        forecast = m.fit(df).predict(future)
        ic(forecast[(forecast['playoff'] + forecast['superbowl']).abs() > 0][
            ['ds', 'playoff', 'superbowl']][-10:])

        m.plot(forecast)
        # plt.show()

        m.plot_components(forecast)
        plt.show()



if __name__ == '__main__':
    Solution().hook()
