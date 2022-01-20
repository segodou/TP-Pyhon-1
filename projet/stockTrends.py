import pandas as pd
from yahoofinancials import YahooFinancials
import datetime
import matplotlib as plt
from pylab import *
import sys
import urllib.request

# On vérifie le nombre d'argument passé au programme. On lit le fichier et on récupère les infos essentielles
if len(sys.argv) != 2:
    sys.exit("ERROR: I need exactly one argument. The URL for the distant text file.")
try:
    with urllib.request.urlopen(sys.argv[1]) as data:
        infos=[]
        for line in data:
            msg = line.decode('utf-8')
            msg = msg.split(':')
            infos.append(msg[1].strip())
except urllib.error.URLError as e:
   print(e.reason)

# Récupération des données sur les prix de l'Ethereum
yahoo_financials = YahooFinancials(infos[1])
data = yahoo_financials.get_historical_price_data(start_date = infos[2], 
                                                  end_date = infos[3], 
                                                  time_interval = infos[4])
eth = pd.DataFrame(data['ETH-USD']['prices'])

# On transforme la date en string
mydate = []
for dat in eth['date']:
    timestam = datetime.datetime.fromtimestamp(dat)
    dat_string = timestam.strftime('%Y-%m-%d')
    mydate.append(dat_string)

# Réalisation du graphique
plt.figure(figsize=(8,5))
plt.plot(mydate, eth['high'], color='red', linestyle='dotted', label='High Price')   # Tracé de la courbe de high price avec texte légende
plt.plot(mydate, eth['low'], color='green', linestyle='dotted',  label='Low Price')   # Tracé de la courbe de low price avec texte légende
plt.plot(mydate, eth['open'], color='blue', label='Open Price')   # Tracé de la courbe de Open price avec texte légende
plt.plot(mydate, eth['close'],color='orange', label='Close Price')   # Tracé de la courbe de Close price avec texte légende
plt.title('Stock prices for Ethereum (USD)')      # Titre
plt.xlabel('Date')                                # Légende abscisse
plt.ylabel('Prices')                              # Légende ordonnée
plt.xticks(rotation = 90)                         # Rotation des dates en abscisse
plt.yticks(range(2054, 5055, 250))                # Interval et pas d'évolution des données en abscisse
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d$')) # Ajout du $ au valeur en ordonnée
plt.legend()                         # Ajout de la légende
plt.show()
