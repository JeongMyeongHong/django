# context, fname, train, test, id, label
from dataclasses import dataclass


@dataclass
class Dataset:
    context: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, value): self._context = value

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, value): self._fname = value

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, value): self._train = value

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, value): self._test = value

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, value): self._id = value

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, value): self._label = value
