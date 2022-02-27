# ScrapingCrypto

## Execution du code 

1. Installer les dépenandes du projet en lançant cette commande : 
``` pip install -r requirements.txt```
2. Lancer main.py : ```python .\main.py```

## Source

Nous avons choisis de récuperer les donnéés depuis l'API : [CoinGecko](https://www.coingecko.com/en/api)

Voici une liste exhaustive des endpoints utilisés par notre projet :

- `simple/supported_vs_currencies` : Récupère les monnaies de comparaisons disponibles sur la source
- `search?query=` : Recherche une cryptomonnaie depuis un mot clé
- `coins/markets` : Récupère les détails d'une cryptomonnaie (selon les paramètres qu'on lui passe).

## L'APPLICATION

1. L'application permet de rechercher une crypto monnaie
2. Elle permet d'enregistrer une liste de cryptomonnaie et une liste de monnaies dans un Json
3. Elle permet d'envoyer un rapport mail des détails de ces cryptomonnaies dans les monnaies choisis

