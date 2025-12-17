# '''Design a class called Album. The class should contain: 
# album_name, number_of_songs, and album_artist attributes.'''
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


# Create a new list called albums1, add five Album objects to it, and print out the 
# list.
albums1 = [
    Album("Album1", 14, "Artist1"),
    Album("Album2", 12, "Artist2"),
    Album("Album3", 5, "Artist3"),
    Album("Album4", 8, "Artist4"),
    Album("Album5", 13, "Artist5"),
]
for album in albums1:
    print(album)

# Sort the albums1 list according to the number_of_songs and print out the list again.
albums1.sort(key=lambda album: album.number_of_songs)
for album in albums1:
    print(album)

# Swap the first and second Album objects in the albums1 list and print out the list again.
albums1[0], albums1[1] = albums1[1], albums1[0]
for album in albums1:
    print(album)

# Create a new list called albums2, add five Album objects to it, and print out the list.
albums2 = [
    Album("Album6", 8, "Artist6"),
    Album("Album7", 11, "Artist7"),
    Album("Album8", 5, "Artist8"),
    Album("Album9", 11, "Artist9"),
    Album("Album10", 10, "Artist10"),
]
for album in albums2: 
    print(album)

# Copy all of the albums from albums1 into albums2.
albums2.extend(albums1)

# Add the following two albums to albums2:
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops! . I Did It Again", 16, "Britney Spears"))

# '''Sort the albums in albums2 alphabetically according to the album name and
# print out the sorted list.'''
albums2.sort(key=lambda album: album.album_name)
for album in albums2:
    print(album)

# '''Search for the album Dark Side of the Moon in albums2 and print out the
# index of the album in the albums2 list.'''
dark_side_index = next((i for i, album in enumerate(albums2) \
if album.album_name == "Dark Side of the Moon"), None)
print(dark_side_index)