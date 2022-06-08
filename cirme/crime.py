from context.domains import *


class Solution(Reader):
    def __init__(self, context):
        self.file = File(context=context)
        # self.reader = Reader()
        self.printer = Printer()
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']

    #  crime_in_seoul
    def save_police_pos(self, fname):
        self.file.fname = fname
        self.printer.dframe(self.csv(self.file))

    #  cctv_in_seoul
    def save_cctv_pos(self, fname):
        self.file.fname = fname
        self.printer.dframe(self.csv(self.file))

    # 구글 맵으로 가져 올꺼라 없음.
    def save_police_norm(self):
        pass

    def folium_test(self):
        pass

    # geo_simple
    def draw_crime_map(self, fname):
        self.file.fname = fname
        self.printer.dframe(self.json(self.file))


if __name__ == '__main__':
    solution = Solution(context='./data/')
    solution.save_police_pos(fname='crime_in_seoul')
    solution.save_cctv_pos(fname='cctv_in_seoul')
    solution.draw_crime_map(fname='geo_simple')
