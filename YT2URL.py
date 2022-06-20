import os

print("\n\n")
print(" __   _______ ___ _   _ ___ _    ")
print(" \ \ / /_   _|_  ) | | | _ \ |   ")
print("  \ V /  | |  / /| |_| |   / |__ ")
print("   |_|   |_| /___|\___/|_|_\____|")
print("                                 ")
print("\n\n")

try:
    from pytube import Playlist
    from art import *
except ModuleNotFoundError:
    print("Downloading packages...")
    os.system('pip install pytube')
    os.system('pip install art')
    print("Please run the program again.")

def get_urls(playlists):
    urls = []
    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            urls.append(url)

    return urls

# CHANGE THE LIST HERE TO THE PLAYLIST YOU WANT THE URL FROM
playlist = ['']

pl_urls = get_urls(playlist)

with open('urls.txt', 'w') as f:
    for url in pl_urls:
        f.write(url+'\n')

print("Done...")