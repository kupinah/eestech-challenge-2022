import os
import numpy
import sys
from matplotlib.font_manager import json_dump
import pandas as pd
import json
import re
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.ensemble import AdaBoostClassifier as ADB
import pickle
from sklearn.model_selection import train_test_split
numpy.set_printoptions(threshold=sys.maxsize)

from typing import List
from joblib import load
import os

class LeakDetection:
    def __init__(self, dirname='./new_model'):
        print(dirname)
        self.model = self.load_model(dirname)

    def load_model(self, dirname):
        """
        Loads your pretrained model to use it for prediction. If no model was build you can ignore this.
        :return:
        """
        return load(os.path.join(dirname, 'new_modell'))

    def predict(self, features: List) -> bool:
        """
        Your implementation for prediction. If leak is detected it should return true.
        :param features: A list of features
        :return: Should return true if leak is detected. Otherwise, it should return false.
        """
        my_features = []
        for i in features[1:]:
            if i == '':
                return True
            my_features.append(i)
        
        pred = self.model.predict([my_features])
        return pred[0] == 1

def generate_steps(freq='10s', amplitude=[0], end_periods=[604800], start_date="2022-03-01", fixed_end=604800):
    """
    Generate the signal. It transforms amplitudes and end periods into timeseries label.
    :param freq: time between each label (this should be fixed to 10s)
    :param amplitude: a list of 0 and 1
    :param end_periods: when amplitude changed in seconds from the start_date
    :return: pandas dataframe with time and label
    """
    end_periods = [int(p/10) * 10 for p in end_periods]
    f = int(freq[:-1])
    idx = pd.date_range(start_date, periods=fixed_end/f, freq=freq)
    ts = pd.Series(idx, name="date")

def read_csv_and_append_labels(csv_file, json):
    base_name = os.path.basename(csv_file)
    
    df = pd.read_csv(csv_file)

    obj = list(filter(lambda x: x['file_name'] == base_name, json['prediction_results']))[0]
    labels = generate_steps(end_periods=obj['end_periods'], amplitude=obj['leakages'])
    df['labels'] = labels['amplitude']
    return df

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def append_targets():
    path = './train_data'
    new_folder = './new_data'
    json_file = open('./results.json')
    json_file = json.load(json_file)
    counter = 0
    lst = sorted_alphanumeric(os.listdir(path))
    for item in lst:
        filepath = os.path.join(path, item)
        df = pd.read_csv(filepath, index_col=None, header = 0)
        row = json_file["prediction_results"][counter]
        changes = row["leakages"]
        ix_of_changes = row["end_periods"]
        if(len(changes) == 1):
            row_of_changes = round(ix_of_changes[0]/10)
            if(row_of_changes == 60480):
                df["Target"] = changes[0]
            else:
                df["Target"] = changes[0]
                df["Target"][row_of_changes:] = int(not changes[0])
        else:
            first_val = round(ix_of_changes[0]/10)
            second_val = round(ix_of_changes[1]/10)

            df["Target"] = 1
            df["Target"][first_val:second_val] = 0
        
        df.to_csv("./new_data/scenario_week_example_" + str(counter) + ".csv")
        counter += 1

def merge_data(path):
    all_files = []
    
    for i in os.listdir(path):
        all_files.append(os.path.join(path, i))
    
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None)
        li.append(df)

    frame = pd.concat(li, axis= 0, ignore_index=True)
    return frame

def delete_first_val():
    path = './new_data'
    path_new = './new_data2'
    for item in os.listdir(path):
        filepath = os.path.join(path, item)
        df = pd.read_csv(filepath)
        first_column = df.columns[0]
        df = df.drop([first_column], axis=1)
        df.to_csv(os.path.join(path_new, item), index=False)

def create_model():
    path = './new_data2'
    dataset = merge_data(path)
    dataset.dropna(inplace=True)

    y = dataset["Target"]
    dataset.drop(['Target','ds'], axis='columns', inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(dataset, y, test_size=0.3)

    fname = "new_model3"
    
    model = RF(n_estimators=4)
    model.fit(X_train.to_numpy(), y_train.to_numpy())
    y_pred = model.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    pickle.dump(model, open(fname, 'wb'))

def all_same(items):
    return all(x == items[0] for x in items)
  

def predict_values():
    path = './test_data'
    model = pickle.load(open('new_modell', 'rb'))
    
    dataset = merge_data(path)
    #dataset.dropna(inplace=True)
    dataset.fillna(0, inplace=True)
    dataset.drop(['ds'], axis='columns', inplace=True)

    res = model.predict(dataset)

    return len(res)

create_model()