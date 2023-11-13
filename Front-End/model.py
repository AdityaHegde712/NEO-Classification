import pandas as pd
import joblib
from os.path import isfile

def predict():
    if isfile('Front-End/uploads/test1.csv'):
        x_test_full = pd.read_csv('Front-End/uploads/test1.csv')
        x_train_full = pd.read_csv('Front-end/resources/train1.csv')
        classifier = joblib.load('models/neo_reg_0.joblib')
        classifier.fit(x_train_full.iloc[:, :-1], x_train_full.iloc[:, -1])

        x_test = x_test_full.iloc[:, :-1]
        y_test = x_test_full.iloc[:, -1]
        y_pred = classifier.predict(x_test)
        return y_pred

print(predict())