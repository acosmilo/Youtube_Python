import urllib
#from pytube import Playlist
import pytube
import moviepy.editor as mp
import os
import time

#Esto es para tener la ruta de trabajo como string
filePath = __file__
absFilePath = os.path.abspath(filePath)
path, filename = os.path.split(absFilePath)

#Esto es un string que devuelve la hora y fecha, sirve para nombrar carpetas
date=(time.strftime("%H-%M-%S-%d-%m-%y"))

#Esto pide al usuario el link de la lista de reproduccion
link=input("Pega el link de la lista de reproduccion: ")

#Se crea una lista usando pytube
p = pytube.Playlist(link)

#Se crea las carpetas de musica y video
os.mkdir(path+'\Musica'+date)
os.mkdir(path+'\Video'+date)


#Definiendo funciones de remplazo de titulos

def ReplaceChars(arg):
    #Esta es la lista de caracteres que seran cambiadas por rayas bajas
    specialChars=[" ","\"","\'","/","(", ")","[","]",".",",",":","/","*","|","#"]
    largo=len(specialChars)
    for i in range(0,largo):
        arg=arg.replace(specialChars[i], "_")
    return arg

# Variable que enumera los clips
i=1

for video in p.videos:
    try:
        #Se transforma el numero i a string
        name=str(i) 
        titulo=ReplaceChars(video.title)

        
        #name=titulo[0:5]
        video.streams.first().download('Video'+date,'Clip_'+name)
        #print(titu)
        
    except (pytube.exceptions.VideoUnavailable, urllib.error.HTTPError, KeyError):
        print('No hay video: '+titulo)
        continue
    
    
    musica=mp.VideoFileClip(path+'\Video'+date+'\Clip_'+ name +'.mp4')
    #os.chdir(path)
    musica.audio.write_audiofile('Musica'+date+'\Audio_'+ name +'.mp3')

    os.rename(path+'\Musica'+date+'\Audio_'+ name +'.mp3',path+'\Musica'+date+'/'+ titulo + name+'.mp3' )
    i=i+1
#audio.download('Musica','Audio_'+titulo)
#print(audio)

#musica=mp.VideoFileClip('Musica/Audio_'+titulo+'.mp4')
#musica.audio.write_audiofile('Musica/Audio_'+titulo+'.mp3')