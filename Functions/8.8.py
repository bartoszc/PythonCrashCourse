def make_album(name, title, tracks=''):
    if tracks:
        return {'band_name': name, 'album_title': title, 'nr_of_tracks': tracks}
    else:
        return {'band_name': name, 'album_title': title}


while True:
    print("(wpisz 'q', aby zakończyć pracę w dowolnym momencie)")
    f_name = input("Band name: ")
    if f_name == 'q':
        break
    l_name = input("Album title: ")
    if l_name == 'q':
        break
    info = make_album(f_name, l_name)
    print(info)

