import pandas as pd
matches = pd.read_csv('matches.csv')
#Question 1. Display all the columns of the sheet of matches
matches.columns
#Question 2. Display total nuumbers of seasons in IPL
pd.unique(matches['season'])
# Question 3. Display unique teams participated in team 2
pd.unique(matches['team2'])
# Question 4. Display unique teams participated in team 1
pd.unique(matches['team1'])
#Question 5 Count the number of matches season wise
matches['season'].value_counts()
#Question 6 Give the counts of the winners as per the team
matches['winner'].value_counts()
#Question 7. Display winning teams for all seasons
matches.drop_duplicates('season', keep = 'last')[['season', 'winner']]
delivery = pd.read_csv('deliveries.csv')
#Question 8. Find the player whose has taken maximum catches
(delivery.groupby('dismissal_kind').get_group('caught'))['player_dismissed'].value_counts().sort_values(ascending = False).head(1)
#Question 9. Display the columns of the table
delivery.columns
#Question 10. Display match_id, ball, batsman, batsman_runs and total_runs
delivery[['match_id', 'ball', 'batsman', 'batsman_runs', 'total_runs']]
#Question 11.Find the batsman scored maximum runs in a particular match
delivery.groupby(['match_id', 'batsman'])['batsman_runs'].sum().sort_values(ascending = False).head()
#Question 12. Print top 5 batsman in descending order as per total runs scored by them
delivery.groupby('batsman')['batsman_runs'].sum().sort_values(ascending = False).head()
