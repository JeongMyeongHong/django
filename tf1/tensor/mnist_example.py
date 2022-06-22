import tensorflow as tf


class Solution(object):
    def __init__(self):
        self.mnist = tf.keras.datasets.mnist  # mnist는 손글씨 데이터셋
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.model = None

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. load data')
            print('2. create model')
            print('3. train and evaluate model')
            print('4. test hand_writing')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                print(self.load_data())
            elif menu == '2':
                print(self.create_model())
            elif menu == '3':
                print(self.train_evaluate_model())
            elif menu == '4':
                print(self.test())
            else:
                break

    def load_data(self):
        mnist = self.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        self.x_train, self.x_test = x_train / 255.0, x_test / 255.0

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),  # input_layer, 무인도에서 천막쳐서 물 모으는것처럼 평평하게 천막 치는거 연상
            tf.keras.layers.Dense(128, activation='relu'),  # hidden_layer, 빗물 필터링할때 물을 모아뒀으니 dense
            tf.keras.layers.Dropout(0.2),  # hidden_layer, 가중치 제거
            tf.keras.layers.Dense(10, activation='softmax')  # output_layer, activation은 식의 역할(지금은..)
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        # sparse <-> dense

    def train_evaluate_model(self):
        self.model.fit(self.x_train, self.y_train, epochs=5)  # epoch : 모델 train 실행 횟수
        self.model.evaluate(self.x_test, self.y_test, verbose=2)
        # verbose : 함수 수행시 발생하는 Log 상세도 0: None, 1: All, 2: less

    def test(self):
        pass


if __name__ == '__main__':
    Solution().hook()
