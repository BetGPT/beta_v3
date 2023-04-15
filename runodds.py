import os
from SbrOddsProvider import SbrOddsProvider
# create an instance of the SbrOddsProvider class
provider = SbrOddsProvider()

# call the get_odds method with the desired file path
file_path = "data/odds.json"
provider.get_odds(file_path)
