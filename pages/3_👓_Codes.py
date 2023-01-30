# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Aknowledgement - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('👓Coding')

st.write(""" ## SQL Codes """)
# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.write(""" At the following links, you can find the SQL codes that are used in this dashboard: 

""")

# SQL Codes
st.write("""
1. https://app.flipsidecrypto.com/velocity/queries/8def6bbf-8602-4dda-99fe-7c66678ceb4a
2. https://app.flipsidecrypto.com/velocity/queries/ea71c087-7514-4698-a196-59e11f900cff
3. https://app.flipsidecrypto.com/velocity/queries/ff770fc6-9628-4231-b74f-e7a654ec2299
4. https://app.flipsidecrypto.com/velocity/queries/559442dc-7200-4d05-9b12-7e627a1a85d1
5. https://app.flipsidecrypto.com/velocity/queries/34c974c7-fb3f-4822-9490-fb9294a01adf
6. https://app.flipsidecrypto.com/velocity/queries/890424b0-58ad-4d56-a0ce-0fe6d27b81d9 
7. https://app.flipsidecrypto.com/velocity/queries/8043d5bb-7e14-4d76-bc4e-75abd59f6348  
8. https://app.flipsidecrypto.com/velocity/queries/3a2c0957-cf4a-4e85-9f19-30004b35be87  
9. https://app.flipsidecrypto.com/velocity/queries/77e334cd-6189-41bc-be48-e45f0683b492


""")
