import streamlit as st
st.set_page_config(page_title="My App", layout="wide")

SELECTIONS = [
    None,
    "Business Intelligence: Overview - Statistics",
    "Business Intelligence: Overview - BUY/SELL By SEC",
    "Business Intelligence: Overview - SEC to BUY/SELL Sankey",
    "Business Intelligence: Order Details - Capacity",
    "Business Intelligence: Order Details - Lifetime",
    "Business Intelligence: Order Details - Price Instruction",
    "Business Intelligence: Time Series - Trades Created Over Time",
    "Anomaly Detection: Plot 1",
    "Anomaly Detection: Plot 2",
    "Anomaly Detection: Plot 3",
    "ASIC Reporting: Plot 1",
    "ASIC Reporting: Plot 2",
    "ASIC Reporting: Plot 3",
    "Future Functionality: Plot 1",
    "Future Functionality: Plot 2",
    "Future Functionality: Plot 3",
    "Future Functionality: Plot 4",
]


if "selections" not in st.session_state:
    st.session_state.selections = None

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
    st.header("Dashboard View Customisation")
    selections = st.multiselect(
        "What are your desired charts",
        SELECTIONS,
        placeholder="Nothing selected yet",
    )

    if st.button("Confirm", icon=":material/arrow_right_alt:"):
        st.session_state.selections = selections
        st.rerun()

# Logout
def logout():
    st.session_state.selections = None
    st.rerun()


selections = st.session_state.selections

logout_page = st.Page(logout, title="Return to Chart Selections", icon=":material/logout:")

# request_1 = st.Page(
#     "request/request_1.py",
#     title="Request 1",
#     icon=":material/help:",
#     default=(role == "Requester"),
# )
# request_2 = st.Page(
#     "request/request_2.py", title="Request 2", icon=":material/bug_report:"
# )
# respond_1 = st.Page(
#     "respond/respond_1.py",
#     title="Respond 1",
#     icon=":material/healing:",
#     default=(role == "Responder"),
# )
# respond_2 = st.Page(
#     "respond/respond_2.py", title="Respond 2", icon=":material/handyman:"
# )
# admin_1 = st.Page(
#     "admin/admin_1.py",
#     title="Admin 1",
#     icon=":material/person_add:",
#     default=(role == "Admin"),
# )
# admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")

# account_pages = [logout_page, settings]
# request_pages = [request_1, request_2]
# respond_pages = [respond_1, respond_2]
# admin_pages = [admin_1, admin_2]

dashboard_page = st.Page(
    "settings.py",
    title="Dashboard",
    default=(selections != None)
)

# Define common element
st.title("BT4013 Capstone: IRESS End-of-Day Summary Dashboard")

# slider_value = st.sidebar.slider(
#     label="Select a value",
#     min_value=0,  # Minimum value of the slider
#     max_value=100,  # Maximum value of the slider
#     value=50,  # Default value of the slider
#     step=1,  # Step size for the slider
# )

# Display the selected value
# st.write("NO LOGO")
# st.write(f"Selected value: {slider_value}")


# page_dict = {}
# if st.session_state.role in ["Requester", "Admin"]:
#     page_dict["Request"] = request_pages
# if st.session_state.role in ["Responder", "Admin"]:
#     page_dict["Respond"] = respond_pages
# if st.session_state.role == "Admin":
#     page_dict["Admin"] = admin_pages

if selections != None:
    pg = st.navigation({"Create Another Dashboard": [logout_page]} | {"Requests":[Reque]})
else:
    pg = st.navigation([st.Page(login)])

pg.run()
