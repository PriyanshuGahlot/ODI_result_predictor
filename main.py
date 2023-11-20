import pandas as pd

dataRaw = pd.read_csv("ODI.csv")
data = dataRaw.drop(["Margin","Match Date", "sno"], axis=1)

team1 = input("Enter name of Team 1: ").capitalize()
team2 = input("Enter name of Team 2: ").capitalize()
ground = input("Ground (type \"any\" if not relevant): ").lower()

count = 0
wins = 0

for i,j,k,winner in zip(data["Team_1"],data["Team_2"],data["Ground"],data["Winner"]):
    if((i==team1 and j==team2) or (i==team2 and j==team1)):
        if(ground=="any" or k == ground):
            count += 1
        if (winner == team1):
            wins += 1

print("Probability of {} winning against {} is {:.3f}".format(team1,team2,wins/count))