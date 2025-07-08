from re import M
import streamlit as st
import pandas as pd
from . import data_fetcher

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
    mf_api = data_fetcher.MutualFundAPI()

    all_schemes = mf_api.get_all_schemes()

    st.multiselect(label="Select Mutual Fund Schemes", options=list(all_schemes.values()), key="scheme_selector")

    selected_scheme_codes = get_selected_scheme_codes(all_schemes)
    selected_scheme_codes_details = [mf_api.get_scheme_details(x) for x in selected_scheme_codes]
    selected_scheme_codes_historical_nav = [mf_api.get_historical_nav(x) for x in selected_scheme_codes]
    
    if selected_scheme_codes:
        # st.write("Selected Scheme Codes:", selected_scheme_codes)
        # st.write("Scheme Details:", selected_scheme_codes_details)
        # st.write("Scheme Historical Nav:", selected_scheme_codes_historical_nav)
        cols = st.columns(len(selected_scheme_codes))
        for index, code_details in enumerate(selected_scheme_codes_details):
            with cols[index]:
                st.subheader(f"{index + 1}: {code_details['scheme_name']}")
                with st.expander("See Details"):
                    st.write(f"Start Date: **{code_details['scheme_start_date']['date']}**")
                    st.write(f"Fund House: **{code_details['fund_house']}**")
                    st.write(f"Scheme Type: **{code_details['scheme_type']}**")
                    st.write(f"Scheme Category: **{code_details['scheme_category']}**")

