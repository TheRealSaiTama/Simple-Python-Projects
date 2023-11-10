from music import playlist
from ascii import logo


def print_playlist():
    for b_index, band in enumerate(playlist, 1):
        name, songs = band
        print(b_index, name)
        for song_num, song in songs:
            print(f"{b_index}:{song_num} {name} - {song}")


def print_song(p_bnumber, p_snumber):
    band_name = playlist[p_bnumber - 1][0]
    song_name = playlist[p_bnumber - 1][1][p_snumber - 1][1]
    print(f"\n{band_name} - {song_name} playing now...")


print(logo)

while True:
    current_play = input("\nSelect a song to play using number:(1:1) ")
    band_number = int(current_play[0])
    song_number = int(current_play[2])
    print_song(band_number, song_number)
    print(f"\n{band_number} - {song_number} playing now...")
    change = input("\nPress C to change the song or any key to quit app:")
    if change == "c":
        continue
    break
print("Good Bye! ")
