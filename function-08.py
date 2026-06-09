def make_album(album_name,artist_name,n_musics=None):
    dic_album = {album_name.title():artist_name.title()}
    if n_musics:
        dic_album["Number of songs"] = n_musics
    return dic_album
while True:
    print("Tell me about the album you want to share ")
    print("(Type 'quit' at any time to quit)")
    album = input("Album name: ")
    if album == "quit":
        break
    artist = input("Artist name: ")
    if artist == "quit":
        break
    number_musics = input("Number of musics in the album: ")
    if number_musics == "quit":
        break
        
    printed_album = make_album(album,artist,number_musics).items()
print(printed_album)
