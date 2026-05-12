import pandas as pd

def durata_in_minuti(durata: str) -> int:
    """
    Converte una durata testuale (es. '2h 50m') in minuti interi.
    """
    h = 0
    m = 0

    if "h" in durata:                   #Controlla se nella stringa c’è la lettera h  
        parti = durata.split("h")       #se si Divide la stringa in due parti, separandola sulla "h"
        h = int(parti[0].strip())       #Prende la parte prima della "h"
        if "m" in parti[1]:
            m = int(parti[1].replace("m", "").strip())  #Rimuove la "m" e converte i minuti in numero.
    elif "m" in durata:
        m = int(durata.replace("m", "").strip())

    return h * 60 + m


def aggiungi_durata_minuti(df: pd.DataFrame) -> pd.DataFrame:#la funzione restituisce un DataFrame.
    """
    Aggiunge la colonna Duration_min convertendo la durata in minuti.
    """
    if "Duration" in df.columns:
        df["Duration_min"] = df["Duration"].apply(durata_in_minuti)
    return df


def aggiungi_feature_temporali(df: pd.DataFrame) -> pd.DataFrame: #la funzione restituisce un DataFrame.
    """
    Aggiunge colonne derivate dalla data del viaggio:
    - Journey_Month
    - Day_of_Week
    - Is_Weekend
    - Season
    """
    if "Date_of_Journey" not in df.columns:
        return df

    df["Journey_Month"] = df["Date_of_Journey"].dt.month
    df["Day_of_Week"] = df["Date_of_Journey"].dt.day_name()
    df["Is_Weekend"] = df["Date_of_Journey"].dt.dayofweek.apply(lambda x: 1 if x >= 5 else 0)

    def stagione(mese):
        if mese in [12, 1, 2]:
            return "Winter"
        elif mese in [3, 4, 5]:
            return "Spring"
        elif mese in [6, 7, 8]:
            return "Summer"
        else:
            return "Autumn"

    df["Season"] = df["Journey_Month"].apply(stagione)

    return df
