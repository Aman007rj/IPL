import streamlit as st
import pickle 
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = ['Rajasthan Royals', 'Royal Challengers Bangalore',
       'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings',
       'Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders',
       'Punjab Kings', 'Mumbai Indians']

cities = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Mumbai(Brabourne)',
       'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah', 'Abu Dhabi', 'Delhi',
       'Chennai', 'Hyderabad', 'Visakhapatnam', 'Chandigarh', 'Bangalore',
       'Jaipur', 'Indore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

st.title('IPL 1st Innings Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs_done = st.number_input('Overs Completed(over > 5)')
with col5:
    wickets = st.number_input('Wickets')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs_done*6)
    wickets_left = 10 - wickets
    crr = current_score/overs_done

    input_df = pd.DataFrame(
        {'BattingTeam' : [batting_team], 'BowlingTeam' : [bowling_team], 'City' : [city],
         'current_score' : [current_score], 'balls_left' : [balls_left], 'wickets_left' : [wickets_left],
         'run_rate' : [crr], 'last5_runs' : [last_five]})
    
    result = pipe.predict(input_df)
    st.header('Predicted score is ' + str(int(result[0])-3) + ' - ' + str(int(result[0])+3))



