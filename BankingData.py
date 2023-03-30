import streamlit as st
import pandas as pd

class Banking:
    @staticmethod
    def Bank():
        st.title("welcome to our banking Zaid!")
        st.subheader("now you can validate all your transactions")
        df=pd.read_csv("data.csv")
        st.dataframe(df)
        st.image("./Bankingdata.png")


#Banking.Bank()