from sklearn.datasets import fetch_olivetti_faces
import matplotlib.pylab as plt
from matplotlib import rc, font_manager
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())


class FaceOff:

    def __init__(self):
        self.faces = fetch_olivetti_faces()

    def off(self):
        f, ax = plt.subplots(1, 3)
        FaceOff.combine(ax, self.faces.images[6], 0, "image 1: $x_1$")
        FaceOff.combine(ax, self.faces.images[10], 1, "image 2: $x_2$")
        new_face = 0.7 * self.faces.images[6] + 0.3 * self.faces.images[10]
        FaceOff.combine(ax, new_face, 2, "image 3: $0.7x_1 + 0.3x_2$")
        plt.show()

    @staticmethod
    def combine(ax, file, position, title):
        ax[position].imshow(file, cmap=plt.cm.bone)
        ax[position].grid(False)
        ax[position].set_xticks([])
        ax[position].set_yticks([])
        ax[position].set_title(title)


if __name__ == '__main__':
    FaceOff().off()
