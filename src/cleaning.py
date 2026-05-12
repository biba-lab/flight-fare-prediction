import pandas as pd

def carica_dati(percorso_file: str) -> pd.DataFrame:
    """
    Carica il dataset dei voli da un file Excel.
    """
    return pd.read_excel(percorso_file)


def pulisci_dati(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esegue le principali operazioni di data cleaning:
    - rimozione dei valori mancanti
    - rimozione dei duplicati
    - normalizzazione della colonna Additional_Info
    - conversione delle colonne temporali
    - conversione Total_Stops in numerico
    """

    # 1. Rimozione NA e duplicati
    df = df.dropna()
    df = df.drop_duplicates(keep="first")

    # 2. Normalizzazione Additional_Info
    if "Additional_Info" in df.columns:
        df["Additional_Info"] = df["Additional_Info"].str.lower().str.strip()

    # 3. Conversione Date_of_Journey
    if "Date_of_Journey" in df.columns:
        df["Date_of_Journey"] = pd.to_datetime(df["Date_of_Journey"], format="mixed")

    # 4. Conversione Dep_Time e Arrival_Time
    if "Dep_Time" in df.columns:
        df["Dep_Time"] = pd.to_datetime(df["Dep_Time"], format="%H:%M", errors="coerce")

    if "Arrival_Time" in df.columns:
        df["Arrival_Time"] = pd.to_datetime(df["Arrival_Time"], format="%H:%M", errors="coerce")

    # 5. Conversione Total_Stops → numerico
    if "Total_Stops" in df.columns:
        df["Total_Stops"] = df["Total_Stops"].replace({
            "non-stop": 0,
            "1 stop": 1,
            "2 stops": 2,
            "3 stops": 3,
            "4 stops": 4
        }).astype(int)

    return df
