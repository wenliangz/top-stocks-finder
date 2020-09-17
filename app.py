import streamlit as st
import pandas as pd
import numpy as np

#
st.write("""

# Top Stocks Finder

The table of data below was collected by webscraping both TipRanks.com and Finviz.com
### Features:

The table can be sorted by specific column attributes (by clicking on the column names).

Rows with specific value ranges can also be highlighted using the drop-down category and slider bar.
(Example: One may wish to sort stocks from with the highest 'AvgPT/Curr%' and highlighting stocks with overall 'Ratings' between 8 and 10.)
""")



stock_list = pd.read_csv('Stocks_All_2020-09-15.csv')
tiprank_stock = stock_list.iloc[:,0:-2].copy()
finviz_stock = stock_list.iloc[:,-2:].copy()

st.write('### Select rows to highlight based on:')
column = st.selectbox('',('Current Price','Low PT','Average PT','High PT', 'LowPT/Curr%', 'AvgPT/Curr%', 'HighPT/Curr%', '# Analyst', 'Rating'))

max_range = int(max(tiprank_stock[column]))

st.write('### Range of values to highlight:')
(i,j) = st.slider('', 0, max_range, (0, 0))


def highlight_row(col):
    global i, j, column

    filter = col[column]

    return ['background-color: #DAF6FA']*len(col) if (filter <=j and filter>=i) else ['background-color: white']*len(col)


st.write('### Stocks Price Target from TipRanks.com (Updated: 2020-09-15)\n(Best used in full-screen mode by clicking top-right of table)')
st.dataframe(tiprank_stock.style.apply(highlight_row, axis = 1).format({
    'Current Price':"{:.5}",
    'Low PT': "{:.5}",
    'Avg PT': "{:.5}",
    'High PT': "{:.5}",
    'LowPT/Curr%': "{:.5}",
    'AvgPT/Curr%': "{:.5}",
    'HighPT/Curr%': "{:.5}",
    }).set_properties(**{'text-align': 'right'}), width=None, height=600)

st.info("This web app has been created by Ryan Lu. Feel free to visit http://www.rylu1.com to learn more about me and my other projects.", )