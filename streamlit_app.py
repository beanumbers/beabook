from operator import index

import streamlit as st
import pandas as pd

options = ["Bank & Credit Card Fees",
           "Books,Music,Movies & DVDs",
           "Cash Withdrawal",
           "Child Expenses",
           "Cleaning",
           "Clothes",
           "Credit Card",
           "Doctor, Dentist",
           "Entertainement",
           "Furniture & Electronic",
           "Gifts",
           "Groceries",
           "Grooming & Beauty",
           "Gym, Sports & Recreation",
           "Home Maintenance",
           "Insurance Health",
           "Insurance Vehicles",
           "Insurance Life",
           "Internet",
           "Lawn & Garden",
           "Loss on Foreign Exhange",
           "Mobile Phone",
           "Rent/Mortgage",
           "Transportation Public",
           "Parking",
           "Personal Items",
           "Pets",
           "Pharmacy",
           "Taxi/Rental Car",
           "Restaurant, Coffee & Bars",
           "Subscriptions",
           "School",
           "Travel & Vacation",
           "Uncategorized",
           "Vehicle-Gas",
           "Vehicle-Maintenance"]
st.title("BEA BOOK")

uploaded_file = st.file_uploader("Drop a bank CSV file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    dataframe["category"] = None
    st.data_editor(dataframe, use_container_width=True,hide_index=True,
                   column_config={
                       'category': st.column_config.SelectboxColumn(label=None, width=None,
                                                                    help="Select transaction category", disabled=None,
                                                                    required=True, pinned=None, default=None,
                                                                    options=options)
                   })
