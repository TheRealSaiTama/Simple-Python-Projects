from music import playlist
from ascii import logo

def print_playlist():
    for b_index,band in enumerate(playlist, 1):
        name, songs = band
        print(b_index, name)
        for song_num, song in songs:
            print(f"{b_index}:{song_num} {name} - {song}")

print(logo)
print_playlist()