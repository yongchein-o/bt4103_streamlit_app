import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

SELECTIONS = [
    "One", "Two",
]

# Initialize selections as an empty list in session state
if "selections" not in st.session_state:
    st.session_state.selections = []

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
    selections = st.multiselect(
        "What are your desired charts",
        SELECTIONS,
        placeholder="Nothing selected yet",
    )
    if st.button("Confirm", icon=":material/arrow_right_alt:"):
        st.session_state.selections = selections
        st.rerun()


def logout():
    st.session_state.selections = []
    st.rerun()


selections = st.session_state.selections

logout_page = st.Page(logout, title="Return to Chart Selections", icon=":material/logout:", default=(not bool(selections)))
dashboard_page = st.Page("settings.py", title="Current Dashboard", icon=":material/visibility:", default=(bool(selections)))


# Define common element
st.title("BT4013 Capstone: IRESS End-of-Day Summary Dashboard")
if selections:
    # Display logout option if selections are made
    pg = st.navigation({"": [dashboard_page, logout_page,]})
else:
    # Display login if no selections
    pg = st.navigation([st.Page(login)])


# Run the navigation
pg.run()