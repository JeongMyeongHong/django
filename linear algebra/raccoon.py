import matplotlib.pylab as plt
from scipy import misc  # 패키지 임포트
from matplotlib import rc, font_manager
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())


class Raccoon:

    @staticmethod
    def solution():
        img_rgb = misc.face()  # 컬러 이미지 로드
        print(img_rgb.shape)  # 데이터의 모양
        Raccoon.mola(221, img_rgb, "RGB 컬러 이미지")
        Raccoon.mola(222, img_rgb[:, :, 0], "Red 채널")
        Raccoon.mola(223, img_rgb[:, :, 1], "Green 채널")
        Raccoon.mola(224, img_rgb[:, :, 2], "Blue 채널")
        plt.show()

    @staticmethod
    def mola(a, img_position, sub_title):
        plt.subplot(a)
        plt.imshow(img_position, cmap=plt.cm.gray)  # 채널 출력
        plt.axis("off")
        plt.title(sub_title)


if __name__ == '__main__':
    Raccoon.solution()
