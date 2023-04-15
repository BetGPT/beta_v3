import os
import json
from datetime import datetime
from sbrscrape import Scoreboard


class SbrOddsProvider:
    
    def __init__(self, sportsbook="fanduel"):
        self.games = Scoreboard(sport="NBA").games
        self.sportsbook = sportsbook

    
    def get_odds(self, file_path):
        """Function returning odds from Sbr server's json content and write to a file

        Args:
            file_path (str): Path to the output JSON file

        Returns:
            None
        """
        dict_res = {}
        for game in self.games:
            # Get team names
            home_team_name = game['home_team'].replace("Los Angeles Clippers", "LA Clippers")
            away_team_name = game['away_team'].replace("Los Angeles Clippers", "LA Clippers")
            
            money_line_home_value = money_line_away_value = totals_value = spread_home_value = spread_away_value = None

            # Get money line bet values
            if self.sportsbook in game['home_ml']:
                money_line_home_value = game['home_ml'][self.sportsbook]
            if self.sportsbook in game['away_ml']:
                money_line_away_value = game['away_ml'][self.sportsbook]
            
            # Get totals bet value
            if self.sportsbook in game['total']:
                totals_value = game['total'][self.sportsbook]

            # Get spread bet values
            if self.sportsbook in game['home_spread']:
                spread_home_value = game['home_spread'][self.sportsbook]
            if self.sportsbook in game['away_spread']:
                spread_away_value = game['away_spread'][self.sportsbook]
            
            dict_res[home_team_name + ':' + away_team_name] =  { 
                'under_over_odds': totals_value,
                home_team_name: { 'money_line_odds': money_line_home_value, 'spread_odds': spread_home_value }, 
                away_team_name: { 'money_line_odds': money_line_away_value, 'spread_odds': spread_away_value }
            }
        
        with open(file_path, 'w') as f:
            json.dump(dict_res, f)
