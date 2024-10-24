import streamlit as st
import datetime

st.set_page_config(page_title="My App", layout="wide")

SELECTIONS = [
    "BI: Overview - Statistics",
    "BI: Overview - BUY/SELL By SEC",
    "BI: Overview - SEC to BUY/SELL Sankey",
    "BI: Order Details - Capacity",
    "BI: Order Details - Lifetime",
    "BI: Order Details - Price Instruction",
    "BI: Time Series - Number Of Trades Over Time",
    "BI: Time Series - Value Of Trades Over Time",
    "Anomaly Detection: Container 1 - Plot 1",
    "Anomaly Detection: Container 1 - Plot 2",
    "Anomaly Detection: Container 1 - Plot 3",
    "ASIC Reporting: Container 1 - Plot 1",
    "ASIC Reporting: Container 1 - Plot 2",
    "ASIC Reporting: Container 1 - Plot 3",
    "Future Functionality: Container 1 - Plot 1",
    "Future Functionality: Container 1 - Plot 2",
    "Future Functionality: Container 2 - Plot 1",
    "Future Functionality: Container 2 - Plot 2",
]

# Initialize selections as an empty list in session state
if "selections" not in st.session_state:
    st.session_state.selections = []
# Initialize date as None in session state
if "date" not in st.session_state:
    st.session_state.date = None

def update_multiselect_style():
    st.markdown(
        """
        <style>
            .stMultiSelect [data-baseweb="tag"] {
                height: fit-content;
            }
            .stMultiSelect [data-baseweb="tag"] span[title] {
                white-space: normal; max-width: 100%; overflow-wrap: anywhere;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
update_multiselect_style()


def login():
    st.header("Dashboard View Customization")
    today = datetime.datetime.now()
    date = st.date_input("Select the date for the report", max_value = today, value=None)
    selections = st.multiselect(
        "Select the desired chart(s)",
        SELECTIONS,
        placeholder="Nothing selected yet",
    )
    if st.button("Confirm", icon=":material/arrow_right_alt:"):
        st.session_state.selections = selections
        st.session_state.date = date
        st.rerun()


def logout():
    st.session_state.selections = []
    st.session_state.date = None
    st.rerun()

# Declare selections and conn
selections = st.session_state.selections
date = st.session_state.date

# conn = st.connection("my_database")
# df = conn.query("select * from trial")
# st.dataframe(df)

logout_page = st.Page(
    logout,
    title="Return to Chart Selections",
    icon=":material/logout:",
    default=(not bool(selections) or not bool(selections)),
)
dashboard_page = st.Page(
    "settings.py",
    title="Current Dashboard",
    icon=":material/visibility:",
    default=(bool(selections) and bool(date)),
)


# Define common element
st.title("Capstone Project: End-of-Day Summary Dashboard")
if selections and (date is not None):
    # Display logout option if selections are made
    pg = st.navigation(
        {
            "": [
                dashboard_page,
                logout_page,
            ]
        }
    )
else:
    # Display login if no selections
    pg = st.navigation([st.Page(login)])


# Run the navigation
pg.run()
