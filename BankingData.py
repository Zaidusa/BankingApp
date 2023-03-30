import streamlit as st
import pandas as pd

class Banking:
    @staticmethod
    def Bank():
        st.title("welcome to our banking Zaid!")
        st.subheader("now you can validate all your transactions")
        df=pd.read_excel("data.xlsx",sheet_name="Sheet1",engine="openpyxl")
        st.dataframe(df)
        st.image("./Bankingdata.png")


#Banking.Bank()