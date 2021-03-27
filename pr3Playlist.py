import urllib
#from pytube import Playlist
import pytube
import moviepy.editor as mp
import os
import time

filePath = __file__
absFilePath = os.path.abspath(filePath)
path, filename = os.path.split(absFilePath)

date=(time.strftime("%H-%M-%S-%d-%m-%y"))


link=input("Pega el link de la lista de reproduccion: ")
#yt = YouTube(link)
p = pytube.Playlist(link)

#audio=yt.streams.filter(file_extension='mp4',only_audio=True).first()
#audio=yt.streams.get_audio_only()

#audio=yt.streams.first()
#titulo=yt.title

os.mkdir(path+'\Musica'+date)
os.mkdir(path+'\Video'+date)


#Definiendo funciones de remplazo de titulos

def ReplaceChars(arg):
    specialChars=[" ","\"","\'","/","(", ")","[","]",".",",",":","/","*","|","#"]
    largo=len(specialChars)
    for i in range(0,largo):
        arg=arg.replace(specialChars[i], "_")
    return arg


i=1
for video in p.videos:
     
    
    try:
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