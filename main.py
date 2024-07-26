from instaloader import Instaloader
import instaloader
from moviepy.editor import VideoFileClip
import os 
import time
import  pygame
L= Instaloader()
# https://www.instagram.com/reel/C9xUBtRNwxE/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==


def insta_to_video(post_utl):
  short_code  = post_utl.split('/')[-2]
  post = instaloader.Post.from_shortcode(L.context,short_code)
  # download the video 
  video = L.download_post(post, target=short_code)
  video_file= None
  post_audio=None
  for file in os.listdir(short_code):
      if file.endswith(".mp4"):
          video_file = os.path.join(short_code, file)
          break
      
  if video_file:
    video= VideoFileClip(video_file)
    audio=video.audio

    #  save audio file
    audio_file = f"{short_code}_audio.mp3"
    audio.write_audiofile(audio_file)

    # close audio and video object
    video.close()
    audio.close()


    print(f"video saved as {audio_file}")
    pygame.init()
    print('audio playing')
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
       time.sleep(1)
    
    print('audio finished playing ')

    
  else:
     print('no video found')




insta_to_video("https://www.instagram.com/reel/C9xUBtRNwxE/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")