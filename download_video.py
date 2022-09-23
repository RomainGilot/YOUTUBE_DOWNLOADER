# Développé par Romain GILOT
# Discord : Romainn#0209
# Pour avoir un maximum de renseignement voir le fichier README

import os # Importation de l'OS
from pytube import YouTube # Importation de la librarie
from functions import mp3Downloader, mp4Downloader # Importation des fonctions locales de télécharge

print("""
------------------------------------------------\n
SCRIPT D'INSTALLATION D'UNE VIDÉO YOUTUBE\n
------------------------------------------------\n\n
""")

youtubeURL = input("Saisir une URL Youtube : ") # choix de la vidéo du https jusqu'à la fin de l'id de la vidéo (pas le nom de la chaine)

lienYoutubeURL = YouTube(youtubeURL) 
print("\nTitre de la vidéo : ", lienYoutubeURL.title, "\nNombre de vues : ", lienYoutubeURL.views, "\nAutheur : ", lienYoutubeURL.author)

choixExtension = input("\nChoisir une extension [mp3/mp4] : ") # choix de l'extension

# Boucle tant que les extensions saisies ci-dessus ne sont pas égales à mp3 et mp4
while choixExtension != "mp3" and choixExtension != "mp4":
    choixExtension = input("\nChoisir une extension [mp3/mp4] : ") # choix de l'extension

#1er choix : ici c'est mp4
if(choixExtension == "mp4"):
    resolution = input("\nChoisir la résolution [144 / 360 / 480 / 720] : ") # Choix de la résolution 
    mp4Downloader(resolution, lienYoutubeURL) #appel de la fonction qui télécharge le fichier en mp4
      

#1er choix : ici c'est mp3
if(choixExtension == "mp3"):
    mp3Downloader(lienYoutubeURL) #appel de la fonction qui télécharge le fichier en mp3


