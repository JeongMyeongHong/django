from sklearn.datasets import load_iris


class Iris:
    def __init__(self):
        self.iris = load_iris()

    def make_iris(self):
        return self.iris.data[0, :]


if __name__ == '__main__':
    print(Iris().make_iris())
