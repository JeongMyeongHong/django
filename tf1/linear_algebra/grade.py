import numpy as np
import matplotlib.pyplot as plt


class Solution(object):

    def __init__(self):
        # 1. Training Data Set
        # 공부시간에 따른 점수 데이터
        self.x_data = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 18, 20, 25, 28, 30]).reshape(-1, 1)
        self.t_data = np.array([5, 7, 20, 31, 40, 44, 46, 49, 60, 62, 70, 80, 85, 91, 92, 97, 98]).reshape(-1, 1)

        # 2. Linear Regression Model 정의
        self.W = np.random.rand(1, 1)  # matrix
        self.b = np.random.rand(1)  # scalar

        # 6. learning rate 정의 = 최초의 보폭
        self.learning_rate = 0.0001

        # 미분을 진행할 loss_func에 대한 lambda 함수를 정의
        self.f = lambda x: self.loss_func(self.x_data, self.t_data, self.W, self.b)

    @staticmethod
    def template():
        model = Solution()
        # 8. 학습종료 후 예측
        model.run()
        print(model.predict(19))  # [[77.86823633]]
        model.show_plt()

    # 3. Loss function
    @staticmethod
    def loss_func(x, t, W, b):
        y = np.dot(x, W) + b
        return np.mean(np.power((t - y), 2))  # 최소 제곱법

    # 4. 미분함수
    @staticmethod
    def numerical_derivative(f, x):
        # f : 미분하려고 하는 다변수 함수
        # x : 모든 변수를 포함하고 있는 ndarray
        delta_x = 1e-4
        # 미분한 결과를 저장할 ndarray
        derivative_x = np.zeros_like(x)

        # iterator를 이용해서 입력된변수 x들 각각에 대해 편미분 수행
        it = np.nditer(x, flags=['multi_index'])

        while not it.finished:
            idx = it.multi_index  # iterator의 현재 index를 tuple 형태로 추출

            # 현재 칸의 값을 잠시 저장
            tmp = x[idx]

            x[idx] = tmp + delta_x
            fx_plus_delta = f(x)  # f(x + delta_x)

            x[idx] = tmp - delta_x
            fx_minus_delta = f(x)  # f(x - delta_x)

            # 중앙치분방식
            derivative_x[idx] = (fx_plus_delta - fx_minus_delta) / (2 * delta_x)

            # 데이터 원상 복구
            x[idx] = tmp

            it.iternext()

        return derivative_x

    # 5. prediction
    # 학습종료 후 임의의 데이터에 대한 예측값을 알아오는 함수
    def predict(self, x):
        return np.dot(x, self.W) + self.b  # Hypothesis, Linear Regression Model

    def run(self):
        learning_rate = self.learning_rate
        # 7. 학습 진행
        # 반복해서 W와 b를 업데이트하며 학습 진행
        for step in range(90000):
            self.W = self.W - learning_rate * self.numerical_derivative(self.f, self.W)  # W의 편미분
            self.b = self.b - learning_rate * self.numerical_derivative(self.f, self.b)  # b의 편미분

            if step % 9000 == 0:
                print('W : {}, b : {}, loss : {}'
                      .format(self.W, self.b, self.loss_func(self.x_data, self.t_data, self.W, self.b)))

    def show_plt(self):
        x_data = self.x_data
        t_data = self.t_data

        # 데이터의 분포를 scatter로 확인
        plt.scatter(x_data.ravel(), t_data.ravel())
        plt.plot(x_data.ravel(), np.dot(x_data, self.W) + self.b)  # 직선
        plt.show()


if __name__ == '__main__':
    Solution.template()



    ### 결과 ###
    # W : [[0.70258102]], b : [0.34989893], loss : 2901.873645506518
    # W : [[3.69624857]], b : [7.76428816], loss : 115.3569040150161
    # W : [[3.48105486]], b : [11.79738967], loss : 96.72058839761921
    # W : [[3.36122244]], b : [14.04325595], loss : 90.94163038784045
    # W : [[3.29449276]], b : [15.29388535], loss : 89.14962619750266
    # W : [[3.25733378]], b : [15.99030879], loss : 88.59394141613679
    # W : [[3.23664149]], b : [16.37811799], loss : 88.42162843946696
    # W : [[3.22511881]], b : [16.59407279], loss : 88.36819569679594
    # W : [[3.21870231]], b : [16.71432903], loss : 88.35162667196388
    # W : [[3.21512923]], b : [16.78129472], loss : 88.34648876269387
