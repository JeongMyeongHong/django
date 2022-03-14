import pandas

from titanic.domains import Dataset
import numpy as np
import pandas as pd
import sklearn


class Model:
    dataset = Dataset()

    def new_model(self, payload, index_col) -> pandas.core.frame.DataFrame:
        this = self.dataset
        this.context = './data/'  # 경로 설정
        this.fname = payload
        return pd.read_csv(this.context + this.fname, index_col=index_col)
