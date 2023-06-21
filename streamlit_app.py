import streamlit as st
import FinanceDataReader as fdr

code = st.text_input("종목 코드를 입력해주세요")
data = fdr.DataReader(code)
st.write(data)