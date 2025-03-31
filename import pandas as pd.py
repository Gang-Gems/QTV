import pandas as pd

file_path = r"C:\Users\vdant\Documents\DIGITAL HUMANITIES BOLOGONA\KNOWLEDGE REPRESENTATION AND EXTRACTION\LGBTQ-Rep\final_dataset.csv"

with open(file_path, "r", encoding="utf-8") as f:
    for i in range(5):  # Legge le prime 5 righe
        print(f.readline())
        
# Prova con diversi delimitatori
df = pd.read_csv(file_path, sep=";", encoding="utf-8")  
print(df.head())  # Mostra le prime righe

