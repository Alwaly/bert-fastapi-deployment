# bert-fastapi-deployment

## Description
#### Ce projet est une demo d'un déploiement de model bert existant au niveau du hub de huggingFace utilisant FastAPI

#### Dans le fichier
##### models.py
Se trouve le model permettant la saisie et l'envoie de notre texte

##### utils.py 
Se trouve notre fonction permettant de charger notre model et notre tokenizer

##### demo-fastAPI.py
Se trouve l'ensemble du code permettant d'appeler les différents fonctions afin de faire une prédiction

## Voici la commande permettant de lancer l'éxécution
### uvicorn demo-fastAPi:app --reload