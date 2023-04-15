import requests
from bs4 import BeautifulSoup
import json

def get_roster_data():
    url = "https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    content_div = soup.find("div", {"class": "mw-parser-output"})
    list_items = content_div.find_all("li")
    
    rosters = {}

    for item in list_items:
        team_link = item.find("a", title=True)
        if team_link and "roster" in team_link['title']:
            team = team_link['title'].replace(" roster", "")
            rosters[team] = []

    for team in rosters.keys():
        team_url = f"https://en.wikipedia.org/wiki/{team.replace(' ', '_')}_roster"
        team_response = requests.get(team_url)
        team_soup = BeautifulSoup(team_response.content, "html.parser")
        team_table = team_soup.find("table", {"class": "sortable"})
        
        if team_table:
            players = team_table.find("tbody").find_all("tr")

            for player in players[1:]:
                player_link = player.find("a", title=True)
                if player_link:
                    player_name = player_link['title']
                    rosters[team].append(player_name)

    return rosters

def save_to_json(data, file_name):
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    rosters = get_roster_data()
    save_to_json(rosters, "nba_rosters.json")
