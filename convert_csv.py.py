import pandas as pd  # Assicurati di importare Pandas

# Carica il file CSV con il delimitatore corretto (;)
df = pd.read_csv("final_dataset.csv", delimiter=";")

# Salva il file con il nuovo delimitatore (,)
df.to_csv("final_dataset_comma.csv", index=False, sep=",", encoding="utf-8")

print("✅ Conversione completata! File salvato come: final_dataset_comma.csv")
