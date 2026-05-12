
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def prepara_dati_model(df: pd.DataFrame, features: list, target: str):
    X = df[features]
    y = df[target]
    X = pd.get_dummies(X)
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0, test_size=0.2)
    return train_X, val_X, train_y, val_y

def addestra_random_forest(train_X, train_y):
    modello = RandomForestRegressor(random_state=1)
    modello.fit(train_X, train_y)
    return modello

def valuta_modello(modello, val_X, val_y):
    pred = modello.predict(val_X)
    mae = mean_absolute_error(val_y, pred)
    return mae
