def make_album(name, title, tracks=''):
    if tracks:
        return {'band_name': name, 'album_title': title, 'nr_of_tracks': tracks}
    else:
        return {'band_name': name, 'album_title': title}


print(make_album('Rammstein', 'Sehnsuht'))
print(make_album('Seal', 'Seven'))
print(make_album('The Doors', 'Strange Days'))
print(make_album('Rammstein', 'Mutter', '11'))
