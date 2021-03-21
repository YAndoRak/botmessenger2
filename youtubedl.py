from __future__ import unicode_literals
import youtube_dl
from moviepy.editor import *
import os



ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
ydlaudio = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
def find_ydl_url(url):
    print("ICI C Ligne 10 find_ydl_url")
    with ydl:
        result = ydl.extract_info(
            url,
            download=False # We just want to extract the info
        )

    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result

    video_urls = video['formats']
    for video_url in video_urls:
        if video_url['format_id'] == '18' :
            print('=================================== 360 P ====================================')
            print('Extension : {}'.format(video_url['ext']))
            print('URL : {}'.format(video_url['url']))
            print('Fomart ID: {}'.format(video_url['format_id']))
            print('Fomart : {}'.format(video_url['format']))
            print('Filesize : {}'.format(video_url['filesize']))
            print('=================================== 360 P ====================================')
            return video_url
ydlaud = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

def find_ydl_url_test(url):
    print("ICI C Ligne 36 find_ydl_url_test")
    with ydl:
        result = ydl.extract_info(
            url,
            download=False # We just want to extract the info
        )

    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result

    video_urls = video['formats']
    for video_url in video_urls:
        print (video_url)
ydlaud = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

def find_ydl_url(url):
    print("ICI C Ligne 55 find_ydl_url 2 mtovy")
    with ydl:
        result = ydl.extract_info(
            url,
            download=False # We just want to extract the info
        )

    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result

    video_urls = video['formats']
    for video_url in video_urls:
        if video_url['format_id'] == '18' :
            print('=================================== 360 P ====================================')
            print('Extension : {}'.format(video_url['ext']))
            print('URL : {}'.format(video_url['url']))
            print('Fomart ID: {}'.format(video_url['format_id']))
            print('Fomart : {}'.format(video_url['format']))
            print('Filesize : {}'.format(video_url['filesize']))
            print('=================================== 360 P ====================================')
            return video_url
ydlaud = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})


def find_audio_url(url_audio):
    print("ICI C Ligne 81 find_audio_url")
    with ydlaud:
        resultat = ydlaud.extract_info(
            url_audio,
            download=False # We just want to extract the info
        )

    if 'entries' in resultat:
        audio = resultat['entries'][0]
    else:
        audio = resultat

    audio_urls = audio['formats']
    for audio_url in audio_urls:
        if audio_url['ext'] == 'm4a' :
            print('=================================== M4a ====================================')
            print('Extension : {}'.format(audio_url['ext']))
            print('URL : {}'.format(audio_url['url']))
            print('Fomart ID: {}'.format(audio_url['format_id']))
            print('Fomart : {}'.format(audio_url['format']))
            print('Filesize : {}'.format(audio_url['filesize']))
            print('=================================== M4a ====================================')
            return audio_url

def download_video(url):
    print("ICI C Ligne 107 download_video")
    ydl_opts = {
        'outtmpl': './tmp/video/%(title)s.%(ext)s',
        'format': '18/best',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        input = ydl.prepare_filename(info_dict)

    return input

def download_audio(url):
    print("ICI C Ligne 120 download_audio")
    ydl_opts = {
        'outtmpl': './tmp/audio/%(title)s.%(ext)s',
        'format': '18/best',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        input = ydl.prepare_filename(info_dict)

    output = '{}mp3'.format(input[:-3])
    video = VideoFileClip(os.path.join(input))
    video.audio.write_audiofile(os.path.join(output))
    url = {
        "input": input,
        "output": output
    }
    return url



if __name__ == "__main__":

    output = find_ydl_url_test('https://fr.pornhub.com/view_video.php?viewkey=ph5d94bf491e8cd')
    print(output)

