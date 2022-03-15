from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemplates:
    def __init__(self, train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self._titanic_model = TitanicModel(train_fname, test_fname)

    @property
    def titanic_model(self): return self._titanic_model
