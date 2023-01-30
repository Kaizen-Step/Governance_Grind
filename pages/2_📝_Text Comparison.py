# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image
# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Text Review - Governance Grind',
                   page_icon=':bar_chart:', layout='wide')
st.title('📝Text Comparison')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.text(" \n")
st.text(" \n")
st.write(""" ## Passed Proposal """)

st.write(""" Two proposals on Terra governance that have been submitted recently and can be good examplars of merits and demerits of a proposal have been analyzed in this report. The first one that is going to be discussed with the proposal ID 3665 was submitted late 2022, and the title is "Contro Protocol Grant Proposal". you can read the whole propsal below this review. It is well written regarding to the technical terms. It prefaces with a concise introduction about the protocol and the reason behind the need for granting the project. Moreover, an alluring claim has been made about how profitable this project can be to the LUNA; they declare that one-tenth of the income will be paid in the aforementioned token. Altogether, the proposal is consistent and brags reasonable offers besides every detail being discussed with enough clarity. """)

st.image(Image.open('Images/Passed_1.jpg'))

st.image(Image.open('Images/Passed_vote.jpg'))

st.image(Image.open('Images/Passed_Validators.jpg'))

st.text(" \n")
st.text(" \n")

st.write(""" ## Rejected Proposal """)
st.write("""
 Meanwhile, another proposal with ID 3795, titled "Terra Poker Grant Proposal (Updated)", which might sound interesting, but is not adequately developed. Although the proposal is written decently, it does not illustrate the project in detail. The idea sounds a little green, and it is not written in a convincing way that could persuade experts to feel confident enough with the amount of grant they have asked.
In conclusion, the passed proposal is written more technically, and the way that the grant would be spended is demonstrated plainly. In contrast, the other submission is ambiguous about how the grant is going to be used, and lacks proficiency.
""")


st.image(Image.open('Images/Rejected_Text.jpg'))

st.image(Image.open('Images/Rejected_Validators.jpg'))
