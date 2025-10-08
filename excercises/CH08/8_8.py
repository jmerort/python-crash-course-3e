"""
8-8
User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album's artist and title. Once you have that
information, call make_album() with the user's input and print the dictionary
that's created. Be sure to include a quit value in the while loop.

@jmerort
Oct 2025
"""


def make_album(artist_name, title, n_songs=None):
    album = {}
    album['artist'] = artist_name.title()
    album['title'] = title.title()
    if n_songs:
        album['n_songs'] = n_songs

    return album

while True:
    print("Name an album that you like:\n(enter 'q' to quit.)")
    title = input("Title: ")
    if title == 'q':
        break
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = make_album(artist, title)

    print(f"Your chosen albums is {album['title']} by {album['artist']}.\n")