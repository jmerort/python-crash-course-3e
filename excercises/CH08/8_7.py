"""
8-7
Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.

@jmerort
Oct 2025
"""

def make_album(artist_name, title, n_songs=None):
    album = {}
    album['artist_name'] = artist_name.title()
    album['title'] = title.title()
    if n_songs:
        album['n_songs'] = n_songs

    return album

album1 = make_album('Judas Priest', 'Painkiller')
album2 = make_album('Peste Noire', 'L\'Ordure à l\'état Pur')
album3 = make_album('Jethro Tull', 'A Passion Play', 1)
print("Some of my favourite albums are:")
print(
    f"{album1['title']} by {album1['artist_name']},\n"
    f"{album2['title']} by {album2['artist_name']},\n"
    f"and {album3['title']} by {album3['artist_name']} which has only {album3['n_songs']} song."
    )