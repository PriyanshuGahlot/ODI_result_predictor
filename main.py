#streamlit
import streamlit as sl
from streamlit_lottie import st_lottie as lottie

animUrl = "https://lottie.host/f1498ac9-bd7e-4376-a663-63d775cc190a/H5Uy0TeYgB.json"

sl.set_page_config(page_title="Result Predictor",layout="wide",page_icon="🏏")

with sl.container():
    sl.title("ODI Result Predictor")
    sl.subheader("Calculates the probability of a team winning using data of all ODI matches since 1987.")

left,right = sl.columns((3,2))

with right:
    lottie(animUrl)

with left:
    sl.markdown("##")
    team1 = sl.text_input("Enter name of Team 1",placeholder="Team 1").strip().title()
    team2 = sl.text_input("Enter name of Team 2",placeholder="Team 2").strip().title()
    ground = sl.text_input("Ground (type \"any\" if not relevant): ",placeholder="Ground").strip().title()

#calculations
import pandas as pd

dataRaw = pd.read_csv("ODI.csv")
data = dataRaw.drop(["sno"], axis=1)

count = 0
wins = 0
allMatches = []

for i,j,k,winner,margin,date in zip(data["Team_1"],data["Team_2"],data["Ground"],data["Winner"],data["Margin"],data["MatchDate"]):
    if((i==team1 and j==team2) or (i==team2 and j==team1)):
        if(ground=="Any" or k == ground):
            count += 1
            allMatches.append(winner+" won by a margin of "+margin+" on "+date+".")
            if (winner == team1):
                wins += 1

with left:
    if(team1!="" and team2 != "" and ground != ""):
        sl.write("##")
        sl.write("Total matches played between {} and {} are {}".format(team1,team2,count))
        sl.write("Total matches won by {} are {}".format(team1,wins))
        if(count>0):
            sl.write("Probability of {} winning against {} is {:.3f}".format(team1, team2, wins / count))
            showBtn = sl.button("Show all Matches")
            if(showBtn):
                for match in allMatches:
                    sl.markdown("- "+match)