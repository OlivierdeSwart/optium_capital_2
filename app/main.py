import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app.data_loader import load_excel_files
from app.report_generator import generate_report

# Load data once when the app starts
df = load_excel_files('data/raw')

st.title("Financial Report Generator")

entity_input = st.text_input("Enter ENTITY_IDs separated by commas:")

if st.button("Search"):
    ids = [e.strip() for e in entity_input.split(",") if e.strip()]
    report = generate_report(df, ids)
    st.dataframe(report)

st.caption(f"{len(df):,} rows loaded from Excel files.")

# st.write(df[['entity_id', 'visa fees', 'mastercard fees']].head())

# st.subheader("🔍 Data Sanity Checks")

# # 1. How many months are in each file?
# if 'month' in df.columns:
#     months_per_entity = df.groupby('entity_id')['month'].nunique()
#     max_months = months_per_entity.max()
#     st.write(f"✅ Max number of months per ENTITY_ID: {max_months}")
#     st.write("ENTITY_IDs with more than 1 month:")
#     st.write(months_per_entity[months_per_entity > 1])

# # 2. Check for duplicate rows per ENTITY_ID + Month
# if {'entity_id', 'month'}.issubset(df.columns):
#     dupes = df.duplicated(subset=['entity_id', 'month'])
#     st.write(f"⚠️ Duplicates by ENTITY_ID + Month: {dupes.sum()}")

# # 3. Unique ENTITY_IDs per file (approximate via value counts)
# st.write("🔢 Top ENTITY_ID frequencies:")
# st.write(df['entity_id'].value_counts().head(10))