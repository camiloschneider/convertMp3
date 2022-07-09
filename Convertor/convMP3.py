from moviepy.editor import *

video = VideoFileClip("pruebaVideo.mp4")
audio = video.audio
audio.write_audiofile('audioPrueba.mp3')
