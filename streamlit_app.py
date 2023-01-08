import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
import datetime
import time
import os

# Get data from API
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Get data from API and convert to dataframe
def get_data_to_df(url):
    data = get_data(url)
    df = pd.DataFrame(data)
    return df

# Get data from API and convert to dataframe
def get_data_to_df_with_pagination(url, page_size, page_number):
    url = url + '?pageSize=' + str(page_size) + '&pageNumber=' + str(page_number)
    data = get_data(url)
    df = pd.DataFrame(data)
    return df

# Get data from API and convert to dataframe
def get_data_to
