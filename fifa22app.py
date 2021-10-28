import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data_file = 'fifa22data.csv'
df = pd.read_csv(data_file, index_col='FullName')

new_df = df.loc[['Lionel Messi','Stephen Black']][['PaceTotal','ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal','PhysicalityTotal']]

categories = list(new_df.columns)

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=new_df.iloc[0],
      theta=categories,
      fill='toself',
      name=new_df.index[0]
))

fig.add_trace(go.Scatterpolar(
        r=new_df.iloc[1],
        theta=categories,
        fill='toself',
        name=new_df.index[1]
  ))

fig.update_layout(
      title= f"{new_df.index[0]} vs {new_df.index[1]}",
      polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]
      )),
    showlegend=True
  )

st.plotly_chart(fig)