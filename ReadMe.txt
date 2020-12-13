Le projet Sie est une application SPA basé sur les frameworks Django de python et la libraisrie reactJs 
fonctionnant sur une architecture basé entièrement sur des services.
Le projet contient plusieurs modules 


### Côté serveur ###

1. Créer un environnement virtuel
2. Se rendre dans le dossier de notre choix puis git clône du projet 
    puis taper la commande pip install > requirements.txt
    attendre qu'il installe toutes dépendance côté python
3. configurer le fichier settings.py dans le dossier minepded qui se trouve dans backen/minepde/minepded
    nommer la bb "sie" et mettez les bons identifiants pour votre bdd postgres
4. Puis dans le dossier backend/minepded ou se trouve le manage.py et lancer la commande "python manage.py migrate" une fois les migrations terminer, 
    lancer le serveur django avec "python manage.py runserver"
    
 """ côté frontEnd React """
 
 1. Se rendre dans le dossier frontend/gui puis lancer la commande "npm install" ou "yarn" pour installer les dépendance 
 2. puis taper "npm run dev" ou "yarn dev" pour lancer le projet sur le port 3000
