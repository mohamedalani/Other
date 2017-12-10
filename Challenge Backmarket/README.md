# Challenge BackMarket

## Principe du challenge 
Le challenge consiste à matcher une liste de produits orthographiée par des clients via des alertes aux réels produits du site internet. 
Nous utilisons une simple approche basée sur la distance de Levenshtein.
Les explications de l'approche sont disponibles directement sur le notebook.

## Requirements 
un seul package est à installer pour pouvoir faire tourner le code (Distance), à installer via `requirements.txt` :

```$ pip install -r requirements.txt```

## Fichiers nécessaires  
Les fichiers csv avec les produits + alertes (changer le chemin dans le notebook si nécessaire) en 4 langues

## Output
Fichiers csv de correspondance alertes > 7 top produits correspondants en 4 langues