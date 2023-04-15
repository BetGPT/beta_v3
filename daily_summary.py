import json
from datetime import datetime

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def generate_daily_summary(odds_data, playoffs_data):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    daily_summary = f"Today's NBA games and betting odds as of {current_datetime}:\n\n"

    for matchup, odds in odds_data.items():
        teams = matchup.split(":")
        daily_summary += f"{teams[0]} vs. {teams[1]}\n"
        daily_summary += f"- {teams[0]}: ({odds[teams[0]]['money_line_odds']}), ({odds[teams[0]]['spread_odds']})\n"
        daily_summary += f"- {teams[1]}: ({odds[teams[1]]['money_line_odds']}), ({odds[teams[1]]['spread_odds']})\n"
        daily_summary += f"- Total: {odds['under_over_odds']}\n\n"

    daily_summary += "Playoffs index information:\n\n"
    for item in playoffs_data:
        daily_summary += f"Title: {item['title']}\n"
        daily_summary += f"Subtitle: {item['subtitle']}\n"
        daily_summary += f"Content: {' '.join(item['content'])}\n\n"

    return daily_summary

if __name__ == "__main__":
    odds_data = json.loads(open_file('data/odds.json'))
    playoffs_data = json.loads(open_file('data/scraped_data.json'))
    daily_summary = generate_daily_summary(odds_data, playoffs_data)
    save_file('data/scratchpad.txt', daily_summary)
