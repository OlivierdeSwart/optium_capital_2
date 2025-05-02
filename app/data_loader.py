import pandas as pd
import os

def clean_currency(value):
    if isinstance(value, str):
        value = value.replace('$', '').replace(' ', '').replace(',', '.').strip()
        try:
            return float(value)
        except ValueError:
            return 0.0
    return value

def load_excel_files(folder_path):
    dfs = []
    for file in os.listdir(folder_path):
        if not file.endswith('.xlsx'):
            continue

        path = os.path.join(folder_path, file)
        try:
            # ✅ Force ENTITY_ID to load as string, preserving leading zeros
            df = pd.read_excel(
                path,
                skiprows=3,
                engine='openpyxl',
                dtype={'ENTITY_ID': str}
            )
            df.columns = df.columns.str.strip().str.lower()

            # No ENTITY_ID modification — preserve original formatting
            if 'entity_id' in df.columns:
                df['entity_id'] = df['entity_id'].str.strip()

            # Drop rows missing key data
            df = df[df['entity_id'].notna() & df['visa fees'].notna()]
            df = df.dropna(how='all')

            # Clean and convert currency fields
            for col in ['visa fees', 'mastercard fees', 'visa sales', 'mastercard sales']:
                if col in df.columns:
                    df[col] = df[col].apply(clean_currency)

            dfs.append(df)
            print(f"✅ Loaded {len(df)} rows from {file}")
        except Exception as e:
            print(f"❌ Skipped {file}: {e}")

    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
