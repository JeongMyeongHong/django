import numpy as np
from tensorflow import keras
from icecream import ic


class Solution:
    def __init__(self):
        self.mnist = keras.datasets.mnist

        (train_images, self.train_labels), (test_images, self.test_labels) = keras.datasets.mnist.load_data()
        train_images = train_images.reshape((60000, 28, 28, 1))
        test_images = test_images.reshape((10000, 28, 28, 1))

        # 픽셀 값을 0~1 사이로 정규화합니다.
        self.train_images, self.test_images = train_images / 255.0, test_images / 255.0
        self.model = keras.models.Sequential()

    def solution(self):
        self.modeling()
        self.training()

    def modeling(self):
        model = self.model
        model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(keras.layers.MaxPooling2D((2, 2)))
        model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D((2, 2)))
        model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(64, activation='relu'))
        model.add(keras.layers.Dense(10, activation='softmax'))
        model.summary()

    def training(self):
        model = self.model
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(self.train_images, self.train_labels, epochs=5)


if __name__ == '__main__':
    ic(np.shape(Solution().solution()))

