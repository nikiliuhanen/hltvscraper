import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from datetime import date
import time

datee=[]
team1=[]
team2=[]
finalResult1=[]
finalResult2=[]
tournament=[]
linkStatsList=[]
playersPlayers=[]
kdPlayers=[]
adrPlayers=[]
kastPlayers=[]
ratingPlayers=[]
datePlayers=[]
team1Players=[]
team2Players=[]
finalResult1Players=[]
finalResult2Players=[]
tournamentPlayers=[]
playerteamPlayers=[]
mapPlayers = []
overallKillsPlayers = []
overallDeathsPlayers = []
overallKill_DeathPlayers = []
overallKill_RoundPlayers = []
overallRoundsWithKillsPlayers = []
overallKillDeathDiffPlayers = []
openingTotalKillsPlayers = []
openingTotalDeathsPlayers = []
openingKillRatioPlayers = []
openingKillRatingPlayers = []
openingTeamWinPercentAfterFirstKillPlayers = []
openingFirstKillInWonRoundsPlayers = []
months = {
    'January':'01',
    'February':'02',
    'March':'03',
    'April':'04',
    'May':'05',
    'June':'06',
    'July':'07',
    'August':'08',
    'September':'09',
    'October':'10',
    'November':'11',
    'December':'12'
}


matchesLinks = []
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


start_date = '2023-10-05'
today = date.today()
end_date = today
print(end_date)



#https://www.hltv.org/results?startDate=2023-10-05&endDate=2024-01-23
def get_results():

    # teams = ['10973/anonymo', '10737/honoris', '10854/los-kogutos', '8068/ago','10278/9ine', '8813/illuminar', '8248/pact',]
    results_url = f"https://www.hltv.org/results?startDate={start_date}&endDate={end_date}"
    t1 = time.perf_counter()
    time.sleep(1)
    page = results_url
    data = requests.get(page, headers = headers)
    print(data.status_code)
    data = BeautifulSoup(data.content, 'html.parser')
    for div in data.findAll('div', attrs={'class':'results'}):
        for a in div.findAll('a', attrs={'class': 'a-reset'}):
            link = a['href']
            matchesLinks.append(link)
    print(matchesLinks)

# def collect_data_results():
#     for link in matchesLinks:
        
#         if (link[:8]=="/matches"):
#             url='https://www.hltv.org'+link
            
#             asd = requests.get(url, headers=headers)
#             print(asd.status_code)
#             asd = BeautifulSoup(asd.content)
            
#             for div in asd.findAll('div', attrs={'class':'match-page'}):
                
                


test = get_results()
# test2 = collect_data_results()