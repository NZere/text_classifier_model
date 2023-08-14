import pickle
import numpy as np
import pandas as pd
import os


class TextClassifier:

    @classmethod
    def load_model(self, path='text_classifier/finalized_model.sav'):
        path = os.path.dirname(os.path.abspath(__file__)) + '/finalized_model.sav'
        return pickle.load(open(path, 'rb'))

    @classmethod
    def predict_index(self, s):
        a = np.array([s])
        classifier = TextClassifier.load_model()
        return classifier.predict(a)[0]


