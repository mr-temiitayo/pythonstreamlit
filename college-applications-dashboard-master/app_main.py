"""
Miguel Antonio H. Germar, 2022
Main script for the College Applications Dashboard.
"""

import pandas as pd
import numpy as np
import streamlit as st

# For connecting to private Google Sheets file
from google.oauth2 import service_account
from gsheetsdb import connect

# Custom imports for app features
from app_home import feature_home
from app_overview import feature_overview
from app_filter_rank import feature_filter_rank
from app_college import feature_college
from app_methodology import feature_methodology
import app_general_functions as agf

if __name__ == "__main__":

    emoji = ":school:"

    st.set_page_config(
        page_title = "ASHS College Apps Dashboard",
        page_icon = emoji,
        initial_sidebar_state = "expanded",
    )

    st.title(f"{emoji} ASHS College Apps Dashboard")

    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )
    conn = connect(credentials = credentials)

    # Dictionary containing sheet names and their respective URLs
    sheets_urls = st.secrets["private_gsheets_url"]

    @st.cache_data(ttl = None)
    def get_data():
        """Obtain data used by the app."""

        # This dictionary will contain both data sheets
        db = {}

        for sheet_name in sheets_urls:
            url = sheets_urls[sheet_name]

            # Query the Google Sheets file.
            query = f'SELECT * FROM "{url}"'

            rows = conn.execute(
                query,
                headers = 1,
            )

            # DataFrame from query
            df = pd.DataFrame(rows)

            db[sheet_name] = df

        db = pd.Series(db)

        # Cast columns to appropriate types, based on data dictionary
        for index, row in db.ddict.iterrows():
            if row["initially_present"]:
                db.main[row["var_name"]] = (
                    db.main[row["var_name"]]
                    .astype(row["primitive_type"])
                )

        # Merge colleges sheet into main sheet
        db.main = (
            db.main
            .merge(
                right = db.colleges,
                on = "name",
                how = "left",
            )
        )

        # Pivot out the locations into bool columns
        unique_locs = db.ddict.loc[
            db.ddict["info_type"] == "location"
        ]

        for index, row in unique_locs.iterrows():
            db.main[row["var_name"]] = db.main["location"] == row["long_name"]

        # Make new sheet with number of applications per student
        db["apps"] = (
            db.main
            .pivot_table(
                index = ["respondent_code", "college_type"],
                values = "index",
                aggfunc = "count",
            )
            .reset_index(drop = False)
            .rename(columns = {"index": "num_apps"})
        )

        # Make new sheet with number of students who chose each option in each college
        checkbox_info_types = ["interests", "characteristics"]
        reference_df = db.ddict.loc[
            db.ddict["info_type"].isin(checkbox_info_types)
        ]
        bool_cols = reference_df.loc[:, "var_name"].tolist()

        college_stats = (
            db.main
            .pivot_table(
                index = ["name"],
                values = bool_cols,
                aggfunc = "sum",
            )
            .reset_index(drop = False)
        )

        college_stats = pd.melt(
            college_stats,
            id_vars = ["name"],
            value_vars = bool_cols,
            var_name = "var_name",
            value_name = "num_students",
        )

        db["college_stats"] = college_stats

        return db

    # Obtain data.
    db = get_data()

    with st.sidebar:
        page_names = {
            "page_home": "Home Page",
            "page_methodology": "Methodology and Recommendations",
            "page_overview": "Overview Charts",
            "page_filter": "Filter and Rank Colleges",
            "page_college": "College Info Charts",
        }

        # Radio buttons to select pages of the app
        feature = st.radio(
            "App Feature",
            options = page_names.keys(),
            format_func = lambda key: page_names[key],
        )

    if feature == "page_home":
        feature_home()

    elif feature == "page_methodology":
        feature_methodology()

    elif feature == "page_overview":
        feature_overview(db)

    elif feature == "page_filter":
        feature_filter_rank(db)

    elif feature == "page_college":
        feature_college(db)