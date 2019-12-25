from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# Function for collecting stats

def get_stats(year, min_games_played=20):
    url = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'.format(year)
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    soup.findAll('tr', limit=2)

    # creating array with all the stats included
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

    # Cleaning stats

    # There are some players with multiple columns because they were traded
    # Remove columns for players on multiple teams by checking for "TOT"
    # Using total season stats instead of on one team
    # Also remove players that played fewer than 20 games
    # There were also empty lists in the data so I removed those
    good_player_stats = []
    player_duplicate = False
    temp_duplicate_player = ""
    viable_player_stats = [] # create list of players that played in the previous year, since lists must match up

    for i in player_stats:
        if i:  # list is not empty and player has played more than 20 games
            if (not player_duplicate) and (int(i[4]) >= min_games_played):  # the player is not repeated
                good_player_stats.append(i)
                viable_player_stats.append(i[0])
                if "TOT" in i:
                    player_duplicate = True
                    temp_duplicate_player = i[0]
            else:
                if not (i[0] == temp_duplicate_player):
                    player_duplicate = False
                    if int(i[4]) >= min_games_played:
                        good_player_stats.append(i)
                        viable_player_stats.append(i[0])
                        if "TOT" in i:
                            player_duplicate = True
                            temp_duplicate_player = i[0]

    # Getting per and ensuring lists are correct
    # Same soup making process but for advanced stats
    url_ws = 'https://www.basketball-reference.com/leagues/NBA_{}_advanced.html'.format(year + 1)
    html_ws = urlopen(url_ws)
    soup_ws = BeautifulSoup(html_ws, features='html.parser')
    soup_ws.findAll('tr', limit=2)

    rows_ws = soup_ws.findAll('tr')[1:]
    player_ws = [[td.getText() for td in rows_ws[i].findAll('td')] for i in range(len(rows_ws))]

    good_player_ws = []
    player_duplicate_ws = False
    temp_duplicate_player_ws = ""
    viable_player_ws = []

    # Iterate through list to remove empty lists, stats i don't care about, and rookies
    for i in player_ws:
        if i and (i[0] in viable_player_stats): # not empty and not a rookie and more than 20 games
            if not player_duplicate_ws and int(i[4]) >= min_games_played:
                good_player_ws.append([i[0], i[21]])
                viable_player_ws.append(i[0])
                if "TOT" in i:
                    player_duplicate_ws = True
                    temp_duplicate_player_ws = i[0]
            else:
                if not (i[0] == temp_duplicate_player_ws):
                    player_duplicate_ws = False
                    if int(i[4]) >= min_games_played:
                        good_player_ws.append([i[0], i[21]])
                        viable_player_ws.append(i[0])
                        if "TOT" in i:
                            player_duplicate_ws = True
                            temp_duplicate_player_ws = i[0]

    # create new player stats list that includes only the players that also played in the following season
    final_player_stats = []
    for i in good_player_stats:
        if i[0] in viable_player_ws:
            final_player_stats.append(i)

    return [final_player_stats, good_player_ws]



# creating stats header
# headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# headers = headers[1:]
# headers.append("PER")


# Gather data for a range of seasons

def gather_for_years(start,end):
    temp_stats = []
    temp_ws = []

    for i in range(start, end):
        this_year_stats = get_stats(i)
        temp_stats.extend(this_year_stats[0])
        for player in this_year_stats[1]:
            temp_ws.append(player[1])

    return[temp_stats, temp_ws]


gather = gather_for_years(2000, 2018)

stats = pd.DataFrame(gather[0])
stats['WS'] = gather[0]

stats.to_csv('player_stats.csv', encoding='utf-8', index=False)
