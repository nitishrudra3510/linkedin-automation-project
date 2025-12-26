"""Streamlit dashboard showing basic metrics."""
import streamlit as st
from dashboard.analytics import acceptance_rate, daily_performance

st.title('LinkedIn Automation Dashboard')

sent_csv = 'data/sent_requests.csv'
responses_csv = 'data/responses.csv'
logs_csv = 'data/logs.csv'

st.header('Key Metrics')
acc = acceptance_rate(sent_csv, responses_csv)
st.metric('Acceptance / Response Rate (%)', f'{acc}%')

st.header('Logs by Day')
perf = daily_performance(logs_csv)
if perf.empty:
    st.info('No logs yet')
else:
    st.dataframe(perf)

st.markdown('This dashboard is a lightweight visual for local runs. Refresh to update.')
