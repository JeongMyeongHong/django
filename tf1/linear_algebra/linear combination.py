import numpy as np
from PIL import Image
from sklearn.datasets import fetch_olivetti_faces
import matplotlib.pylab as plt
from matplotlib import rc, font_manager
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())


class LinearCombination:

    @staticmethod
    def combine():
        faces = fetch_olivetti_faces()
        f, ax = plt.subplots(1, 3)
        ax[0].imshow(faces.images[6], cmap=plt.cm.bone)
        ax[0].grid(False)
        ax[0].set_xticks([])
        ax[0].set_yticks([])
        ax[0].set_title("image 1: $x_1$")
        ax[1].imshow(faces.images[10], cmap=plt.cm.bone)
        ax[1].grid(False)
        ax[1].set_xticks([])
        ax[1].set_yticks([])
        ax[1].set_title("image 2: $x_2$")
        new_face = 0.5 * faces.images[6] + 0.5 * faces.images[10]
        ax[2].imshow(new_face, cmap=plt.cm.bone)
        ax[2].grid(False)
        ax[2].set_xticks([])
        ax[2].set_yticks([])
        ax[2].set_title("image 3: $0.7x_1 + 0.3x_2$")
        plt.show()

    @staticmethod
    def combine_exam(image1, image2):
        ratio = 0.4
        f, ax = plt.subplots(2, 2)
        ax[0, 0].imshow(image1, cmap=plt.cm.bone)
        ax[0, 0].grid(False)
        ax[0, 0].set_xticks([])
        ax[0, 0].set_yticks([])
        ax[0, 0].set_title("image 1: $x_1$")
        ax[0, 1].imshow(image2, cmap=plt.cm.bone)
        ax[0, 1].grid(False)
        ax[0, 1].set_xticks([])
        ax[0, 1].set_yticks([])
        ax[0, 1].set_title("image 2: $x_2$")
        new_face = ratio * image1 + (1-ratio) * image2
        ax[1, 0].imshow(new_face.astype('uint8'), cmap=plt.cm.bone)
        ax[1, 0].grid(False)
        ax[1, 0].set_xticks([])
        ax[1, 0].set_yticks([])
        ax[1, 0].set_title(f'image 3: ${ratio}x_1 + {round((1-ratio), 1)}x_2$')
        new_face2 = (1-ratio) * image1 + ratio * image2
        ax[1, 1].imshow(new_face2.astype('uint8'), cmap=plt.cm.bone)
        ax[1, 1].grid(False)
        ax[1, 1].set_xticks([])
        ax[1, 1].set_yticks([])
        ax[1, 1].set_title(f'image 4: ${ratio}x_1 + {round((1-ratio), 1)}x_2$')
        plt.show()

    @staticmethod
    def load_image(file_name):
        return np.array(Image.open(file_name))


if __name__ == '__main__':
    # LinearCombination.combine()
    file_name1 = 'data/전신.png'
    file_name2 = 'data/아이언맨.png'
    LinearCombination.combine_exam(LinearCombination.load_image(file_name1), LinearCombination.load_image(file_name2))
    LinearCombination.combine_exam(
        LinearCombination.load_image('data/1.png'), LinearCombination.load_image('data/2.png'))
