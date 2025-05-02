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