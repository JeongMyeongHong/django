from sklearn.datasets import load_digits  # 패키지 임포트
import matplotlib.pylab as plt
from matplotlib import rc, font_manager
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())


class ClassNumber:
    def __init__(self):
        self.digits = load_digits()  # 데이터 로드
        self.samples = [0, 10, 20, 30, 1, 11, 21, 31]  # 선택된 이미지 번호
        self.d = [self.digits.images[self.samples[i]] for i in range(8)]

    def class_number(self):
        plt.figure(figsize=(8, 2))
        [ClassNumber.show_plot(data=self.d, index=i, aspect=1) for i in range(8)]
        plt.suptitle("숫자 0과 1 이미지")
        plt.tight_layout()
        plt.show()
        plt.savefig('./save/class_number.png')

    def vector_image(self):
        v = [self.d[i].reshape(64, 1) for i in range(8)]  # 벡터화
        plt.figure(figsize=(8, 3))
        [ClassNumber.show_plot(data=v, index=i, aspect=0.4) for i in range(8)]
        plt.suptitle("벡터화된 이미지", y=1.05)
        plt.tight_layout(w_pad=7)
        plt.show()
        plt.savefig('./save/vector_image.png')

    @staticmethod
    def show_plot(data, index, aspect):
        plt.subplot(1, len(data), index + 1)
        plt.imshow(data[index], aspect=aspect, interpolation='nearest', cmap=plt.cm.bone_r)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.title("image {}".format(index + 1))


if __name__ == '__main__':
    ClassNumber().class_number()
    ClassNumber().vector_image()
