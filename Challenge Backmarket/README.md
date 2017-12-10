# Challenge BackMarket

## Principe du challenge 
Le challenge consiste � matcher une liste de produits orthographi�e par des clients via des alertes aux r�els produits du site internet. 
Nous utilisons une simple approche bas�e sur la distance de Levenshtein.
Les explications de l'approche sont disponibles directement sur le notebook.

## Requirements 
un seul package est � installer pour pouvoir faire tourner le code (Distance), � installer via `requirements.txt` :

```$ pip install -r requirements.txt```

## Fichiers n�cessaires  
Les fichiers csv avec les produits + alertes (changer le chemin dans le notebook si n�cessaire) en 4 langues

## Output
Fichiers csv de correspondance alertes > 7 top produits correspondants en 4 langues