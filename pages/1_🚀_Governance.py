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
st.set_page_config(page_title='Goveranance - Governance Grind',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Governance')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Governance_Grind1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8043d5bb-7e14-4d76-bc4e-75abd59f6348/data/latest')
    elif query == 'Governance_Grind2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/890424b0-58ad-4d56-a0ce-0fe6d27b81d9/data/latest')
    elif query == 'Governance_Grind3':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/34c974c7-fb3f-4822-9490-fb9294a01adf/data/latest')
    elif query == 'Governance_Grind4':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/559442dc-7200-4d05-9b12-7e627a1a85d1/data/latest')
    elif query == 'Governance_Grind5':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ff770fc6-9628-4231-b74f-e7a654ec2299/data/latest')
    elif query == 'Governance_Grind6':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ea71c087-7514-4698-a196-59e11f900cff/data/latest')
    elif query == 'Governance_Grind7':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8def6bbf-8602-4dda-99fe-7c66678ceb4a/data/latest')
    return None


Governance_Grind1 = get_data('Governance_Grind1')
Governance_Grind2 = get_data('Governance_Grind2')
Governance_Grind3 = get_data('Governance_Grind3')
Governance_Grind4 = get_data('Governance_Grind4')
Governance_Grind5 = get_data('Governance_Grind5')
Governance_Grind6 = get_data('Governance_Grind6')
Governance_Grind7 = get_data('Governance_Grind7')
Most_popular_contracts = get_data('Most_popular_contracts')

st.subheader('Development Charts')

df = Governance_Grind1
df2 = Governance_Grind2
df3 = Governance_Grind3
df4 = Governance_Grind4
df5 = Governance_Grind5
df6 = Governance_Grind6
df7 = Governance_Grind7
df8 = Most_popular_contracts

# Number of Voters
fig = px.pie(df, values="VOTERS", names="PROPOSAL ID",
             title='Number of Voters', hole=0.5)
fig.update_layout(legend_title='PROPOSAL ID', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Votes
fig = px.pie(df, values="VOTES", names="PROPOSAL ID",
             title='Number of Votes', hole=0.5)
fig.update_layout(legend_title='PROPOSAL ID', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Voters based on each Option
fig = px.bar(df2.sort_values(["PROPOSAL ID", "VOTERS_COUNT"], ascending=[
             True, False]), x="PROPOSAL ID", y="VOTERS_COUNT", color="VOTE_OPTION", title='Number of Voters based on each Option')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Voters")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Votes based on each Option
fig = px.bar(df2.sort_values(["PROPOSAL ID", "VOTES_COUNT"], ascending=[
             True, False]), x="PROPOSAL ID", y="VOTES_COUNT", color="VOTE_OPTION", title='Number of Voters based on each Option')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Votes")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Validators voters
fig = px.pie(df3, values="VOTERS_COUNT", names="PROPOSAL ID",
             title='Validators voters', hole=0.5)
fig.update_layout(legend_title='PROPOSAL ID', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Validators votes
fig = px.pie(df3, values="VOTES_COUNT", names="PROPOSAL ID",
             title='Validators votes', hole=0.5)
fig.update_layout(legend_title='PROPOSAL ID', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Validators Vs Nonvalidators Voters
fig = px.bar(df4.sort_values(["PROPOSAL ID", "VOTERS_COUNT"], ascending=[
             True, False]), x="PROPOSAL ID", y="VOTERS_COUNT", color="STATUS", title='Validators Vs Nonvalidators Voters', barmode='group')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Voters")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Validators Vs Nonvalidators Votes
fig = px.bar(df4.sort_values(["PROPOSAL ID", "VOTES_COUNT"], ascending=[
             True, False]), x="PROPOSAL ID", y="VOTES_COUNT", color="STATUS", title='Validators Vs Nonvalidators Votes', barmode='group')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Votes")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# New User per Proposal
fig = px.bar(df5.sort_values(["PROPOSAL ID", "NEW_VOTERS"], ascending=[
             True, False]), x="PROPOSAL ID", y="NEW_VOTERS", color="PROPOSAL ID", title='New User per Proposal')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of New Voters")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily New User per Proposal
fig = px.bar(df6.sort_values(["DATE", "NEW_VOTERS"], ascending=[
             True, False]), x="DATE", y="NEW_VOTERS", color="PROPOSAL ID", title='Daily New User per Proposal')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of New Voters")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Number of Voters
fig = px.bar(df7.sort_values(["DATE", "VOTERS"], ascending=[
             True, False]), x="DATE", y="VOTERS", color="PROPOSAL ID", title='Daily Number of Voters')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Voters")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Number of Votes
fig = px.bar(df7.sort_values(["DATE", "VOTES"], ascending=[
             True, False]), x="DATE", y="VOTES", color="PROPOSAL ID", title='Daily Number of Votes')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Votes")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


###################################
