import streamlit as st
import pandas as pd
from . import data_fetcher, calculator

st.set_page_config(
    page_title="Mutual Fund Analyzer",
    page_icon=":bar_chart:",
    layout="wide"
)

def get_selected_scheme_codes(all_schemes):
    selected_scheme_names = st.session_state.get("scheme_selector", [])
    if not selected_scheme_names:
        return []

    scheme_name_to_code = {v: k for k, v in all_schemes.items()}
    selected_scheme_codes = [scheme_name_to_code[name] for name in selected_scheme_names]
    return selected_scheme_codes

def main():
    st.title("Mutual Fund Analyzer")

    all_schemes = data_fetcher.mf_api.get_all_schemes()

    st.multiselect(label="Select Mutual Fund Schemes", options=list(all_schemes.values()), key="scheme_selector")

    selected_scheme_codes = get_selected_scheme_codes(all_schemes)
    selected_scheme_codes_details = [data_fetcher.mf_api.get_scheme_details(x) for x in selected_scheme_codes]
    
    if selected_scheme_codes:
        st.write("Selected Scheme Codes:", selected_scheme_codes)
        st.write("Scheme Details:", selected_scheme_codes_details)

