import streamlit as st
import pandas as pd

df = pd.read_csv("dashboard_keywords_full.csv")

st.title('Pacific-Blue Dashboard')

kw = st.selectbox('Choose a keyword:', sorted(df.Keyword.unique()))
tier = st.radio('Meaning tier:', ['Meaning 1', 'Meaning 2', 'Meaning 3'])

subset = df[(df.Keyword == kw) & (df.Tier == tier)]

st.dataframe(subset.style.hide(axis='index'))

if len(subset):
    st.subheader('Verbatim Excerpts')
    for row in subset.itertuples():
        st.markdown(f'**Source {row.Top_Sources}**  \n> {row.Sample_Verbatim}')
