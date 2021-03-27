from pytube import YouTube
import moviepy.editor as mp

link=input("Pega el link del video: ")
yt = YouTube(link)
#audio=yt.streams.filter(file_extension='mp4',only_audio=True).first()
#audio=yt.streams.get_audio_only()
audio=yt.streams.first()
titulo=yt.title

audio.download('Musica','Audio_'+titulo)
print(audio)

clip=mp.VideoFileClip('Musica/Audio_'+titulo+'.mp4')
clip.audio.write_audiofile('Musica/Audio_'+titulo+'.mp3')