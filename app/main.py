import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import io
from app.data_loader import load_excel_files
from app.report_generator import generate_report

# Load data once when the app starts
df = load_excel_files('data')

st.title("Financial Report Generator")

# Initialize session state for report
if 'report' not in st.session_state:
    st.session_state.report = None
if 'last_input' not in st.session_state:
    st.session_state.last_input = ""

# 🔁 Form input
with st.form("search_form", clear_on_submit=False):
    entity_input = st.text_input("Enter ENTITY_IDs separated by commas:", value=st.session_state.last_input)
    submitted = st.form_submit_button("Search")

# ✅ Handle form submission
if submitted:
    ids = [e.strip() for e in entity_input.split(",") if e.strip()]
    report = generate_report(df, ids)
    st.session_state.report = report
    st.session_state.last_input = entity_input

# ✅ Show report if exists
if st.session_state.report is not None:
    st.dataframe(st.session_state.report)

    # 📥 Excel download
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        st.session_state.report.to_excel(writer, index=True, sheet_name='Report')

    st.download_button(
        label="📄 Download Report (Excel)",
        data=buffer.getvalue(),
        file_name="financial_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # 📊 Monthly Breakdown Toggle
    if 'month' in df.columns:
        show_monthly = st.checkbox("📊 Show month-by-month breakdown", key="show_months")
        if show_monthly:
            monthly = df[df['entity_id'].isin(
                [e.strip() for e in st.session_state.last_input.split(",") if e.strip()]
            )].groupby(['entity_id', 'month'])[
                ['visa fees', 'mastercard fees', 'visa sales', 'mastercard sales']
            ].sum().reset_index()
            st.subheader("Monthly Breakdown")
            st.dataframe(monthly)

# 👇 Show how much data is loaded
st.caption(f"{len(df):,} rows loaded from Excel files.")
