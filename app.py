# To run this app, first install the required libraries:
# pip install pandas pandas-profiling streamlit streamlit-pandas-profiling

import pandas as pd
import streamlit as st

from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = ProfileReport(df)

st_profile_report(pr)
