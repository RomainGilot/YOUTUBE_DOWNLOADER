# Développé par Romain GILOT
# Discord : Romainn#0209
# Pour avoir un maximum de renseignement voir le fichier README

import os # Importation de l'OS
from pytube import YouTube # Importation de la librarie


#Procédure de téléchargement d'une vidéo avec l'extension mp4
def mp4Downloader(resolution, lienYoutubeURL) :  

    while resolution != "144" and resolution != "360" and resolution != "480" and resolution != "720":
        resolution = input("\nErreur : Mauvaise résolution. \nRe-choisir la résolution [144 / 360 / 480 / 720] : ")

    while int(resolution) > 720:
        resolution = input("\nErreur : Mauvaise résolution, elle doit être <= 720p \nRe-choisir la résolution [144 / 360 / 480 / 720] : ")

    mp4_files = lienYoutubeURL.streams.filter(file_extension="mp4") 
    mp4_files = mp4_files.get_by_resolution(resolution + "p")

    print("\nTéléchargement en cours...\n")

    mp4_files.download("Vidéo téléchargé") # Téléchargé la vidéo et la déposé dans Vidéo téléchargé

    print("Vidéo téléchargé\n")

# Procédure de téléchargement d'une musique avec l'extension mp3
def mp3Downloader(lienYoutubeURL):
    mp3_files = lienYoutubeURL.streams.filter(only_audio=True).first()

    print("\nTéléchargement en cours...\n")
    fichier = mp3_files.download("Musique téléchargé")

    base, ext = os.path.splitext(fichier)
    fichierConverti = base + '.mp3'
    os.rename(fichier, fichierConverti)

    print("Musique téléchargé\n")  