import pandas as pd
import os

def load_excel_files(folder_path):
    dfs = []
    for file in os.listdir(folder_path):
        if not file.endswith(".xlsx"):
            continue

        path = os.path.join(folder_path, file)
        try:
            df = pd.read_excel(path, skiprows=3, engine='openpyxl')
            df.columns = df.columns.str.strip().str.lower()
            df = df[df['entity_id'].notna() & df['visa fees'].notna()]
            df = df.dropna(how='all')
            dfs.append(df)
        except Exception as e:
            print(f"❌ Skipping {file} - {e}")
    return pd.concat(dfs, ignore_index=True)