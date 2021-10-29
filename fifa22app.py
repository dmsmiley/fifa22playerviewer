import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data_file = 'fifa22data.csv'
df = pd.read_csv(data_file, index_col='FullName')


#User Selection _____________________________

player_1 = st.selectbox('Select First Player: ', options=list(df.index.values))
player_2 = st.selectbox('Select Second Player: ', options=list(df.index.values),
                        index=1)
                        
#Player Display_________________________________________

photo_1 = df.loc[player_1]['PhotoUrl']


photo_2 = df.loc[player_2]['PhotoUrl']



col1_1, col2_1 = st.columns(2)

with col1_1:
    st.header(player_1)
    st.image(photo_1, use_column_width=True)


with col2_1:
    st.header(player_2)
    st.image(photo_2, use_column_width=True)


#Player Information_____________________________________

club_logo_1 = df.loc[player_1]['Club Logo']
flag_1 = df.loc[player_1]['Flag']

club_logo_2 = df.loc[player_2]['Club Logo']
flag_2 = df.loc[player_2]['Flag']


col1_2, col2_2, col3_2, col4_2 = st.columns(4)

with col1_2:
    st.subheader("Club:")
    st.markdown("##### {}".format(df.loc[player_1]['Club']))
    st.image(club_logo_1, use_column_width=True)
    
with col2_2:
    st.subheader("Nationality:")
    st.markdown("##### {}".format(df.loc[player_1]['Nationality']))
    st.image(flag_1, use_column_width=True)

with col3_2:
    st.subheader("Club:")
    st.markdown("##### {}".format(df.loc[player_2]['Club']))
    st.image(club_logo_2, use_column_width=True)

with col4_2:
    st.subheader("Nationality:")
    st.markdown("##### {}".format(df.loc[player_2]['Nationality']))
    st.image(flag_2, use_column_width=True)

#Main Stats_____________________________________________

new_df = df.loc[[player_1,player_2]][['PaceTotal','ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal','PhysicalityTotal']]

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


#Row 1 Stats______________________________________________





#Sidebar

st.sidebar.markdown("### Need Help Finding a Player?")
country_club = st.sidebar.selectbox('What Country is Their Club In?', list(df['Club Country'].unique()))
league = st.sidebar.selectbox('What League is Their Club in?', list(df['Club League'][df['Club Country'] == country_club].unique()))
club = st.sidebar.selectbox('What Club Do They Play For?', list(df['Club'][df['Club League'] == league].unique())
st.sidebar.selectbox('Who is the Player?', list(df.index[df['Club'] == club]))
