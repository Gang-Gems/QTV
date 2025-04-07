import pandas as pd

try:
    df = pd.read_csv("dataset1_top_down.csv", delimiter=";", encoding="latin1")

    df.to_csv("dataset_top_down.csv", index=False, sep=",", encoding="utf-8")

    print("File salvato come: dataset_top_down.csv")

except FileNotFoundError:
    print("Controlla il nome del file o il percorso.")

